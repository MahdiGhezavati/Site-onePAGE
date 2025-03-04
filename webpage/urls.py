from django.urls import path , include
from webpage.views import *

urlpatterns = [
    path("" , HOME , name="index" ),
]
