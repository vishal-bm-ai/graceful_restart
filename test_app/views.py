from django.shortcuts import render
from django.http import HttpResponse
from .models import Count
import time
# Create your views here.

def test(request):
    for i in range(120):
        Count.objects.create(cnt=i)
        time.sleep(0.5)
    return HttpResponse(f'Hello')

def test(request):
    print("dummy called")
    return HttpResponse(f'Dummy called')
