from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
]