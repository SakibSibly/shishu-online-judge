from django.shortcuts import render
from django.views import View


class ContestsView(View):
    def get(self, request):
        return render(request, 'contests/contests.html')
    
    def post(self, request):
        pass
