from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProblemsView.as_view(), name='problems'),
    path('<int:id>/', views.FetchProblemView.as_view(), name='getproblem'),
]