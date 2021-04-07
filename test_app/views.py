from django.shortcuts import render
from django.http import HttpResponse
from .models import Count

# Create your views here.

def test(request):
    Count.objects.create(cnt=1)
    return HttpResponse(f'Hello')