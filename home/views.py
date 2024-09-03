from django.shortcuts import render, HttpResponse
from django.views import View
import os, subprocess


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')
    
    def post(self, request):
        obj = request.POST
        main_code = obj['code']
        return self.execute_cpp_code(main_code)


    def execute_cpp_code(self, cpp_code):
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(cpp_code)
        
        compile_command = ["g++", cpp_file, "-o", "temp_program"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            return HttpResponse("Compilation failed:\n" + compilation.stderr)
        
        execution_command = ["./temp_program"]
        execution = subprocess.run(execution_command, capture_output=True, text=True)
        

        try:
            if execution.returncode == 0:
                return HttpResponse("Program Output:\n" + execution.stdout)
            else:
                return HttpResponse("Program failed to execute:\n" +execution.stderr)
        finally:
            os.remove(cpp_file)
            os.remove("temp_program")