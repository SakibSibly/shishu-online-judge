from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContestsView.as_view(), name='contests'),
    path('<int:contest_id>/', views.FetchContestView.as_view(), name='fetch_contest'),
]