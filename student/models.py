from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

