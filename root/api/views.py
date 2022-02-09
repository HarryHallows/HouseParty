from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. [ url locations ]

def main(request):
    return HttpResponse("Hello World")
