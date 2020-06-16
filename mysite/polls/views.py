from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello Mofockas")

# Create your views here.
