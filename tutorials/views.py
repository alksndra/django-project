from django.shortcuts import render
from django.http import HttpResponse
from . import  models
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index_name(request, name):
    new_user = models.Name(input_name=name)
    new_user.save()
    return HttpResponse("Hello, %s." % name)


def names_list(request):
    all_names_list = models.Name.objects.all()
    template = loader.get_template('template.html')
    context = {
        'all_names_list': all_names_list,
    }
    return render(request, 'template.html', context)

"""

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
"""



# Create your views here.
