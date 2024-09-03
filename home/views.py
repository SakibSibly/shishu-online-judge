from django.shortcuts import render, HttpResponse
from django.views import View
import os, subprocess


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')
    
    def post(self, request):
        pass