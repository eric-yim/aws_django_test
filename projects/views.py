from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome to my <i>App</i>")
def detail(request, project_id):
    return HttpResponse("You're looking at question %s.".format(project_id))
