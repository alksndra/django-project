from django.shortcuts import render
from django.http import HttpResponse
from . import  models


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index_name(request, name):
    new_user = models.Name(input_name=name)
    new_user.save()
    return HttpResponse("Hello, %s." % name)


def names_list(request):
    return HttpResponse(models.Name.objects.all())



# Create your views here.
