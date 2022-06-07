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

def archive_page(request):
    cat_query = request.GET.get('cat')
    search_query = request.GET.get('search')

    if cat_query:
        cat_obj = Category.objects.get(slug=cat_query)
        students = Student.objects.filter(category=cat_obj)
    elif search_query:
        students = Student.objects.filter(name__icontains=search_query)
    else:
        students = None
    ctx = {"students": students}

    return render(request, 'archive.html', ctx)