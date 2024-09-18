from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import UserRegistrationForm


class UserProfileView(View):
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        return render(request, 'accounts/profile.html' , {'user': user})

    def post(self, request):
        pass


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            institution = form.cleaned_data['institution']
            user = CustomUser.objects.create_user(name=name, username=username, email=email, password=password, country=country, city=city, university=institution)
            user.save()
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})