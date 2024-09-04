from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContestsView.as_view(), name='contests'),
]