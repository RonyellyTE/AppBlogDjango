from django.urls import path, include
from django.http import HttpResponse 
from .views import user_profile_view


urlpatterns = [
    path('profile', user_profile_view)
]
