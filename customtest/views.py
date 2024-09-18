from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from .forms import CodeSubmissionForm
from globals.executor import CodeExecutor


class CustomTest(View):
    def get(self, request):
        form = CodeSubmissionForm()
        context = {
            'form': form
        }
        return render(request, 'customtest/custom.html', context)
    
    def post(self, request):
        if request.user.is_authenticated:
            form = CodeSubmissionForm(request.POST)
            if form.is_valid():
                obj = request.POST
                source_code = obj['code']
                language = obj['language']
                input_data = obj['input_data']

                executor = CodeExecutor()
                context = {}

                if language == "0":
                    output = executor.execute_c_code(source_code, input_data, 1)
                    context = {
                        'output': output[0],
                        'time': "Execution time: " + output[1] + " seconds"
                    }
                elif language == "1":
                    output = executor.execute_cpp_code(source_code, input_data, 1)
                    context = {
                        'output': output[0],
                        'time': "Execution time: " + output[1] + " seconds"
                    }
                elif language == "2":
                    output = executor.execute_python_code(source_code, input_data, 1)
                    context = {
                        'output': output[0],
                        'time': "Execution time: " + output[1] + " seconds"
                    }
                    
                return render(request, 'customtest/output.html', context)
            else:
                return HttpResponse("Invalid Character found in the source code")
        login_url = reverse('login') + '?' + urlencode({'next': request.path})
        return redirect(login_url)
