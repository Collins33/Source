from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

#the welcome view
def welcome(request):
    return HttpResponse("COLLINS NJAU")
