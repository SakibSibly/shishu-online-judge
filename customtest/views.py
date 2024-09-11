from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import CodeSubmissionForm
from globals.executor import CodeExecutor
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
            source_code = obj['code']
            language = obj['language']
            input_data = obj['input_data']

            executor = CodeExecutor()
            context = {}

            if language == "0":
                start_time = time.time()
                output = executor.execute_c_code(source_code, input_data, 1)
                end_time = time.time()
                context = {
                    'output': output,
                    'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
                }
            elif language == "1":
                start_time = time.time()
                output = executor.execute_cpp_code(source_code, input_data, 1)
                end_time = time.time()
                context = {
                    'output': output,
                    'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
                }
            elif language == "2":
                start_time = time.time()
                output = executor.execute_python_code(source_code, input_data, 1)
                end_time = time.time()
                context = {
                    'output': output,
                    'time': "Execution time: " + str(round(end_time - start_time, 4)) + " seconds"
                }
                
            return render(request, 'customtest/output.html', context)
        else:
            return HttpResponse("Invalid Character found in the source code")
