from django.contrib import admin

# Register your models here.
from .models import Student, Category

admin.site.register(Student)
admin.site.register(Category)