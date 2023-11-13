from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import faculties
# from .forms import FacultiesForm

def index(request):
    faculties_list = faculties.objects.all()
    context = {'faculties_list': faculties_list}
    return render(request, 'faculties/index.html', context)

def view_faculties(request, id):
    return HttpResponseRedirect(reverse('index'))