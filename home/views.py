from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Post


class HomeView(View):
    def get(self, request):
        latest_posts = Post.objects.all().order_by('-created_at')[:5]
        context = {
            'latest_posts': latest_posts
        }
        return render(request, 'home/home.html', context)
    
    def post(self, request):
        pass