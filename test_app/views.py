from django.shortcuts import render
from django.http import HttpResponse
from .models import Count
import time
# Create your views here.

def test(request):
    for i in range(120):
        print(i)
        Count.objects.create(cnt=4)
	    time.sleep(1)
    return HttpResponse(f'Hello')
