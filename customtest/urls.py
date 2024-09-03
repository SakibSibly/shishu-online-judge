from django.urls import path
from . import views


urlpatterns = [
    path('', views.CustomTest.as_view(), name='customtest'),
]