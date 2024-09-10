from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import CodeSubmissionForm
import os, subprocess
import time


class CustomTest(View):
    def get(self, request):
        form = CodeSubmissionForm()
        context = {
            'form': form
        }
        return render(request, 'customtest/custom.html', context)
    
    def post(self, request):
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            obj = request.POST
            main_code = obj['code']
            language = obj['language']
            input_data = obj['input_data']

            if language == "0":
                return self.execute_c_code(request, main_code, input_data)
            elif language == "1":
                return self.execute_cpp_code(request, main_code, input_data)
            elif language == "2":
                return self.execute_python_code(request, main_code, input_data)
        else:
            return HttpResponse("Invalid Character found in the source code")
        
    def execute_c_code(self, request, cpp_code, input_data):
        c_file = "main.c"
        with open(c_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["gcc", c_file, "-o", "main"]
        start_time = time.perf_counter()
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        end_time = time.perf_counter()
        
        if compilation.returncode != 0:
            os.remove(c_file)
            context = {
                'output': "Compilation failed:\n" + compilation.stderr,
                'time': "Compilation time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)
        
        execution_command = ["./main"]
        execution = subprocess.run(execution_command, input=input_data, capture_output=True, text=True)
        
        if execution.returncode == 0:
            os.remove(c_file)
            os.remove("main")
            context = {
                'output': execution.stdout,
                'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)
        else:
            os.remove(c_file)
            os.remove("main")
            context = {
                'output': "Program failed to execute:\n" + execution.stderr,
                'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)
        
    def execute_cpp_code(self, request, cpp_code, input_data):
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["g++", cpp_file, "-o", "main"]
        start_time = time.perf_counter()
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        end_time = time.perf_counter()
        
        if compilation.returncode != 0:
            os.remove(cpp_file)
            context = {
                'output': "Compilation failed:\n" + compilation.stderr,
                'time': "Compilation time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)
        
        execution_command = ["./main"]
        execution = subprocess.run(execution_command, input=input_data, capture_output=True, text=True)
        
        if execution.returncode == 0:
            os.remove(cpp_file)
            os.remove("main")
            context = {
                'output': execution.stdout,
                'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)
        else:
            os.remove(cpp_file)
            os.remove("main")
            context = {
                'output': "Program failed to execute:\n" + execution.stderr,
                'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)

    def execute_python_code(self, request, python_code, input_data):
        python_file = "main.py"
        with open(python_file, "w") as file:
            file.write(python_code)
        
        execution_command = ["python", python_file]
        start_time = time.perf_counter()
        execution = subprocess.run(execution_command, input=input_data, capture_output=True, text=True)
        end_time = time.perf_counter()

        if execution.returncode == 0:
            os.remove(python_file)
            context = {
                'output': execution.stdout,
                'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)
        else:
            os.remove(python_file)
            context = {
                'output': "Program failed to execute:\n" + execution.stderr,
                'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
            }
            return render(request, 'customtest/output.html', context)