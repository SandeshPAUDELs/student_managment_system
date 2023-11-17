from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import faculties
from .forms import facultiesForm

def index(request):
    faculties_list = faculties.objects.all()
    # context = {'faculties_list': faculties_list}
    context = {'students': faculties_list} 
    return render(request, 'faculties/index.html', context)

def view_faculties(request, id):
    return HttpResponseRedirect(reverse('index'))



def add(request):
  if request.method == 'POST':
    form = facultiesForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = faculties(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'faculties/add.html', {
        'form': facultiesForm(),
        'success': True
      })
  else:
    form = facultiesForm()
  return render(request, 'faculties/add.html', {
    'form': facultiesForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = faculties.objects.get(pk=id)
    form = facultiesForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'faculties/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = faculties.objects.get(pk=id)
    form = facultiesForm(instance=student)
  return render(request, 'faculties/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = faculties.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))


def student_details(request, id):
    student = faculties(faculties, pk=id)
    student.save()
    return HttpResponseRedirect(reverse('index'))

