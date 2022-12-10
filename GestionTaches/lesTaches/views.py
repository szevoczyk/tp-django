from django.shortcuts import render
from django.http import HttpResponse

from lesTaches.models import Task
from django.template import Template,Context
# Create your views here.


def home(request,name):
    return HttpResponse('bienvenue sur '+name)

def task_listing(request):
    objets=Task.objects.all().order_by('due_date')
    template=Template('{% for elem in objets %} {{elem}} <br />{% endfor %}')
    # print(str(template))
    context=Context({'objets':objets})
    # print(str(template.render(context)))
    return HttpResponse(str(template.render(context)))

def task_listing2(request):
    objets = Task.objects.all().order_by('-due_date')
    return render(request,template_name='list.html', context={'taches':objets})

def task_listing_t(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request,template_name='list.html',context={'taches':tasks})

# def add_task(request):
#     foo_instance = Foo.objects.create(name='test')
#     return render(request, 'some_name.html.html')
    