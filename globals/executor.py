r"""
This module contains the CodeExecutor class which is used to execute the code written by the user.

Supported languages: C, C++, Python
"""

import os
import subprocess


class CodeExecutor():
    """
    This class allows you to execute the code and returns the result as string.
    """

    def execute_c_code(self, source_code: str, input_data: str, time_limit: float) -> str:
        c_file = "main.c"
        with open(c_file, "w") as file:
            file.write(source_code)
        
        compile_command = ["gcc", c_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            os.remove(c_file)
            return "Compilation failed:\n" + compilation.stderr
        
        try:
            execution_command = ["./main"]
            execution = subprocess.run(execution_command, timeout=time_limit, input=input_data, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            os.remove(c_file)
            os.remove("main")
            return "Time Limit Exceeded!"
        except subprocess.CalledProcessError:
            os.remove(c_file)
            os.remove("main")
            return "Program failed to execute"
        except Exception as e:
            os.remove(c_file)
            os.remove("main")
            return "An error occurred: " + str(e)
        
        if execution.returncode == 0:
            os.remove(c_file)
            os.remove("main")
            return execution.stdout
        else:
            os.remove(c_file)
            os.remove("main")
            return "Program failed to execute:\n" + execution.stderr


    def execute_cpp_code(self, source_code: str, input_data: str, time_limit: float) -> str:
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(source_code)
        
        compile_command = ["g++", cpp_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            os.remove(cpp_file)
            return "Compilation failed:\n" + compilation.stderr
        
        try:
            execution_command = ["./main"]
            execution = subprocess.run(execution_command, timeout=time_limit, input=input_data, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            os.remove(cpp_file)
            os.remove("main")
            return "Time Limit Exceeded!"
        except subprocess.CalledProcessError:
            os.remove(cpp_file)
            os.remove("main")
            return "Program failed to execute"
        except Exception as e:
            os.remove(cpp_file)
            os.remove("main")
            return "An error occurred: " + str(e)
        
        if execution.returncode == 0:
            os.remove(cpp_file)
            os.remove("main")
            return execution.stdout
        else:
            os.remove(cpp_file)
            os.remove("main")
            return "Program failed to execute:\n" + execution.stderr
        

    def execute_python_code(self, source_code: str, input_data: str, time_limit: float) -> str:
        python_file = "main.py"
        with open(python_file, "w") as file:
            file.write(source_code)
        

        try:
            execution_command = ["python", python_file]
            execution = subprocess.run(execution_command, timeout=time_limit, input=input_data, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            os.remove(python_file)
            return "Time Limit Exceeded!"
        except subprocess.CalledProcessError:
            os.remove(python_file)
            return "Program failed to execute"
        except Exception as e:
            os.remove(python_file)
            return "An error occurred: " + str(e)
        
        if execution.returncode == 0:
            os.remove(python_file)
            return execution.stdout
        else:
            os.remove(python_file)
            return "Program failed to execute:\n" + execution.stderr
