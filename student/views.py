from django.shortcuts import render

from .forms import AddPostForm
from .models import Student, Category

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

def dashboard_page(request):
    return render(request, "dashboard.html")


def add_student_page(request):

    form = AddPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    ctx = {"form": form}
    return render(request, "student-form.html", ctx)


def edit_student_page(request, id):

    blog = Blog.objects.get(id=id)

    form = AddPostForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()

    ctx = {"form": form}

    return render(request, "student-form.html", ctx)