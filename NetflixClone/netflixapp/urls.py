### APPPP ####
from django.urls import path
from .views import *

app_name = 'netflixapp'

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("profile/", ProfileList.as_view(), name="profile_list")
    
]