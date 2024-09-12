r"""
This module contains the CodeExecutor class which is used to execute the code written by the user.

Supported languages: C, C++, Python
"""

import os
import subprocess
import time


class CodeExecutor():
    """
    This class allows you to execute the code and returns the result as string.
    """

    def execute_c_code(self, source_code: str, input_data: str, time_limit: float) -> list:
        c_file = "main.c"
        with open(c_file, "w") as file:
            file.write(source_code)
        
        compile_command = ["gcc", c_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            os.remove(c_file)
            return ["Compilation failed:\n" + compilation.stderr, "N/A"]
        
        try:
            execution_command = ["./main"]
            start_time = time.time()
            execution = subprocess.run(execution_command, timeout=time_limit, input=input_data, capture_output=True, text=True)
            end_time = time.time()
        except subprocess.TimeoutExpired:
            os.remove(c_file)
            os.remove("main")
            return ["Time Limit Exceeded!", "N/A"]
        except subprocess.CalledProcessError:
            os.remove(c_file)
            os.remove("main")
            return ["Program failed to execute", "N/A"]
        except Exception as e:
            os.remove(c_file)
            os.remove("main")
            return ["An error occurred: " + str(e), "N/A"]
        
        if execution.returncode == 0:
            os.remove(c_file)
            os.remove("main")
            return [execution.stdout, round(end_time - start_time, 3)]
        else:
            os.remove(c_file)
            os.remove("main")
            return ["Program failed to execute:\n" + execution.stderr, "N/A"]


    def execute_cpp_code(self, source_code: str, input_data: str, time_limit: float) -> list:
        cpp_file = "main.cpp"
        with open(cpp_file, "w") as file:
            file.write(source_code)
        
        compile_command = ["g++", cpp_file, "-o", "main"]
        compilation = subprocess.run(compile_command, capture_output=True, text=True)
        
        if compilation.returncode != 0:
            os.remove(cpp_file)
            return ["Compilation failed:\n" + compilation.stderr, "N/A"]
        
        try:
            execution_command = ["./main"]
            start_time = time.time()
            execution = subprocess.run(execution_command, timeout=time_limit, input=input_data, capture_output=True, text=True)
            end_time = time.time()
        except subprocess.TimeoutExpired:
            os.remove(cpp_file)
            os.remove("main")
            return ["Time Limit Exceeded!", "N/A"]
        except subprocess.CalledProcessError:
            os.remove(cpp_file)
            os.remove("main")
            return ["Program failed to execute", "N/A"]
        except Exception as e:
            os.remove(cpp_file)
            os.remove("main")
            return ["An error occurred: " + str(e), "N/A"]
        
        if execution.returncode == 0:
            os.remove(cpp_file)
            os.remove("main")
            return [execution.stdout, round(end_time - start_time, 3)]
        else:
            os.remove(cpp_file)
            os.remove("main")
            return ["Program failed to execute:\n" + execution.stderr, "N/A"]
        

    def execute_python_code(self, source_code: str, input_data: str, time_limit: float) -> list:
        python_file = "main.py"
        with open(python_file, "w") as file:
            file.write(source_code)
        

        try:
            execution_command = ["python", python_file]
            start_time = time.time()
            execution = subprocess.run(execution_command, timeout=time_limit, input=input_data, capture_output=True, text=True)
            end_time = time.time()
        except subprocess.TimeoutExpired:
            os.remove(python_file)
            return ["Time Limit Exceeded!", "N/A"]
        except subprocess.CalledProcessError:
            os.remove(python_file)
            return ["Program failed to execute", "N/A"]
        except Exception as e:
            os.remove(python_file)
            return ["An error occurred: " + str(e), "N/A"]
        
        if execution.returncode == 0:
            os.remove(python_file)
            return [execution.stdout, round(end_time - start_time, 3)]
        else:
            os.remove(python_file)
            return ["Program failed to execute:\n" + execution.stderr, "N/A"]
