from django.shortcuts import render, HttpResponse
from django.views import View
import os, subprocess


class CustomTest(View):
    def get(self, request):
        return render(request, 'customtest/custom.html')
    
    def post(self, request):
        obj = request.POST
        main_code = obj['code']
        language = obj['language']

        if language == "0":
            return self.execute_c_code(main_code)
        elif language == "1":
            return self.execute_cpp_code(main_code)
        elif language == "2":
            return self.execute_python_code(main_code)

    def execute_c_code(self, cpp_code):
        c_file = "main.c"
        with open(c_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["gcc", c_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            return HttpResponse("Compilation failed:\n" + compilation.stderr)
        
        execution_command = ["./main"]
        execution = subprocess.run(execution_command, capture_output=True, text=True)
        
        if execution.returncode == 0:
            os.remove(c_file)
            os.remove("main")
            return HttpResponse("Program Output:\n" + execution.stdout)
        else:
            os.remove(c_file)
            os.remove("main")
            return HttpResponse("Program failed to execute:\n" +execution.stderr)
        
    def execute_cpp_code(self, cpp_code):
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["g++", cpp_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            return HttpResponse("Compilation failed:\n" + compilation.stderr)
        
        execution_command = ["./main"]
        execution = subprocess.run(execution_command, capture_output=True, text=True)
        
        if execution.returncode == 0:
            os.remove(cpp_file)
            os.remove("main")
            return HttpResponse("Program Output:\n" + execution.stdout)
        else:
            os.remove(cpp_file)
            os.remove("main")
            return HttpResponse("Program failed to execute:\n" +execution.stderr)

    def execute_python_code(self, python_code):
        python_file = "main.py"
        with open(python_file, "w") as file:
            file.write(python_code)
        
        execution_command = ["python", python_file]
        execution = subprocess.run(execution_command, capture_output=True, text=True)

        if execution.returncode == 0:
            os.remove(python_file)
            return HttpResponse("Program Output:\n" + execution.stdout)
        else:
            os.remove(python_file)
            return HttpResponse("Program failed to execute:\n" + execution.stderr)