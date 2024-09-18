from django.shortcuts import render
from django.views import View
from .models import CustomUser


class UserProfileView(View):
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        return render(request, 'accounts/profile.html' , {'user': user})

    def post(self, request):
        pass