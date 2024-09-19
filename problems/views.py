from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from .models import Problem, InputOutput, SolvedData
from customtest.forms import CodeSubmissionForm
from globals.executor import CodeExecutor


class ProblemsView(View):
    def get(self, request):
        fetched_problems = Problem.objects.all()
        if request.user.is_authenticated:
            record = SolvedData.objects.filter(user=request.user)
            solved_data = []
            for entry in record:
                solved_data.append(entry.id)
        else:
            solved_data = None
        context = {
            'fetched_problems': fetched_problems,
            'solved_data': solved_data
        }
        return render(request, 'problems/problems.html', context)
    
    def post(self, request):
        pass


class FetchProblemView(View):
    def get(self, request, id):
        problems = Problem.objects.filter(id=id)
        test_cases = InputOutput.objects.filter(problem=problems[0].id)
        context = {
            'fetched_problem': problems,
            'test_cases': test_cases,
            'form': CodeSubmissionForm()
        }
        return render(request, 'problems/individual_problem.html', context)
    
    def post(self, request, id):
        if request.user.is_authenticated:       
            source_code = request.POST['code']
            language = request.POST['language']
            ios = InputOutput.objects.filter(problem=Problem.objects.filter(id=id)[0])
            test_cases = []
            for element in ios:
                test_cases.append([element.input, element.output, element.problem.time_limit])
            

            for case in test_cases:
                executor = CodeExecutor()
                if language == "0":
                    output = executor.execute_c_code(source_code, case[0], case[2])
                elif language == "1":
                    output = executor.execute_cpp_code(source_code, case[0], case[2])
                elif language == "2":
                    output = executor.execute_python_code(source_code, case[0], case[2])

                if executor.compare_outputs(output[0].strip(), case[1].strip()) == False:
                    context = {
                        'output': f"Test case failed:\n\nInput:\n{case[0]}\n\nExpected:\n{case[1]} \n\n\nReceived:\n{output[0]}",
                        'time': "Execution time: " + output[1] + " seconds"
                    }
                    with open("test.txt", "w+") as file:
                        file.write(output[0])
                    with open("test2.txt", "w+") as file:
                        file.write(case[1])
                    
                    return render(request, 'customtest/output.html', context)
        
            context = {
                'output': "All test cases passed",
                'time': "Execution time: " + output[1] + " seconds"
            }

            solved_record = SolvedData(problem=Problem.objects.filter(id=id)[0], user=request.user)
            solved_record.save()
            return render(request, 'customtest/output.html', context)
        
        login_url = reverse('login') + '?' + urlencode({'next': request.path})
        return redirect(login_url)
