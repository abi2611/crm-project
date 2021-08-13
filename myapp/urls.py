from django.urls import path
from myapp. views import example
urlpatterns = [
    path('',example, name="home"),
     
]