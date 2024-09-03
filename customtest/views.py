from django.shortcuts import render, HttpResponse
from django.views import View
import os, subprocess
from .forms import CodeSubmissionForm


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

            if language == "0":
                return self.execute_c_code(request, main_code)
            elif language == "1":
                return self.execute_cpp_code(request, main_code)
            elif language == "2":
                return self.execute_python_code(request, main_code)
        else:
            return HttpResponse("Invalid Character found in the source code")
        
    def execute_c_code(self, request, cpp_code):
        c_file = "main.c"
        with open(c_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["gcc", c_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            os.remove(c_file)
            context = {
                'output': "Compilation failed:\n" + compilation.stderr
            }
            return render(request, 'customtest/output.html', context)
        
        execution_command = ["./main"]
        execution = subprocess.run(execution_command, capture_output=True, text=True)
        
        if execution.returncode == 0:
            os.remove(c_file)
            os.remove("main")
            context = {
                'output': "Program Output:\n" + execution.stdout
            }
            return render(request, 'customtest/output.html', context)
        else:
            os.remove(c_file)
            os.remove("main")
            context = {
                'output': "Program failed to execute:\n" +execution.stderr
            }
            return render(request, 'customtest/output.html', context)
        
    def execute_cpp_code(self, request, cpp_code):
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["g++", cpp_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            os.remove(cpp_file)
            context = {
                'output': "Compilation failed:\n" + compilation.stderr
            }
            return render(request, 'customtest/output.html', context)
        
        execution_command = ["./main"]
        execution = subprocess.run(execution_command, capture_output=True, text=True)
        
        if execution.returncode == 0:
            os.remove(cpp_file)
            os.remove("main")
            context = {
                'output': "Program Output:\n" + execution.stdout
            }
            return render(request, 'customtest/output.html', context)
        else:
            os.remove(cpp_file)
            os.remove("main")
            context = {
                'output': "Program failed to execute:\n" +execution.stderr
            }
            return render(request, 'customtest/output.html', context)

    def execute_python_code(self, request, python_code):
        python_file = "main.py"
        with open(python_file, "w") as file:
            file.write(python_code)
        
        execution_command = ["python", python_file]
        execution = subprocess.run(execution_command, capture_output=True, text=True)

        if execution.returncode == 0:
            os.remove(python_file)
            context = {
                'output': execution.stdout
            }
            return render(request, 'customtest/output.html', context)
        else:
            os.remove(python_file)
            context = {
                'output': "Program failed to execute:\n" + execution.stderr
            }
            return render(request, 'customtest/output.html', context)