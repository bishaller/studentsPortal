from django.shortcuts import render
from .models import Student

# Create your views here.

def index_page(request):
    students = Student.objects.all()
    ctx = {
        'students':students
    }
    return render(request, "index.html", ctx)

def single_page(request, id):
    student = Student.objects.get(id=id)
    ctx = {'student':student}
    return render(request, 'single.html', ctx)