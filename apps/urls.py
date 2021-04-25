from django.urls import path
from .views import AppsFunction

urlpatterns=[
    path('', AppsFunction.as_view()),
]