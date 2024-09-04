from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProblemsView.as_view(), name='problems'),
]