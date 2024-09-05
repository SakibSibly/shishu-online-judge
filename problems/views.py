from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Problem, InputOutput


class ProblemsView(View):
    def get(self, request):
        fetched_problems = Problem.objects.all()
        return render(request, 'problems/problems.html', {'fetched_problems': fetched_problems})
    
    def post(self, request):
        pass


class FetchProblemView(View):
    def get(self, request, id):
        problems = Problem.objects.filter(id=id)
        test_cases = InputOutput.objects.filter(problem=problems[0].id)
        return render(request, 'problems/individual_problem.html', {'fetched_problem': problems, 'test_cases': test_cases})
    
    def post(self, request, number):
        pass