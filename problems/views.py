from django.shortcuts import render
from django.views import View


class ProblemsView(View):
    def get(self, request):
        return render(request, 'problems/problems.html')
    
    def post(self, request):
        pass
    