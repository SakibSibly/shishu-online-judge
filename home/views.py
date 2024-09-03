from django.shortcuts import render, HttpResponse
from django.views import View
import os, subprocess


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')
    
    def post(self, request):
        obj = request.POST
        main_code = obj['code']
        self.execute_cpp_code(main_code)


    def execute_cpp_code(self, cpp_code):
    # Step 1: Save the C++ code to a file
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(cpp_code)
        
        # Step 2: Compile the C++ code
        compile_command = ["g++", cpp_file, "-o", "temp_program"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        # Check for compilation errors
        if compilation.returncode != 0:
            HttpResponse("Compilation failed:")
            HttpResponse(compilation.stderr)
            return
        
        # Step 3: Execute the compiled program
        execution_command = ["./temp_program"]
        execution = subprocess.run(execution_command, capture_output=True, text=True)
        
        # Step 4: Display the output
        if execution.returncode == 0:
            HttpResponse("Program Output:")
            HttpResponse(execution.stdout)
        else:
            HttpResponse("Program failed to execute:")
            HttpResponse(execution.stderr)
        
        # Clean up: Remove temporary files
        os.remove(cpp_file)
        os.remove("temp_program")