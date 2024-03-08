from django.shortcuts import render
from django.http import HttpResponse
import traceback

def index(request):
    
    try:
        return HttpResponse("Hello World!")
    except Exception as e:
        # dummy for Code Scanning 
        return traceback.format_exc()

