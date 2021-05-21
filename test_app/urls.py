from django.urls import path, include
from .views import test, dummy

urlpatterns = [
    path('',test),
    path('app/',dummy),
]
