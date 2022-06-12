from django.urls import path
from .views import index_page, single_page, archive_page, dashboard_page, add_student_page, edit_student_page

urlpatterns = [
    path('', index_page, name='index'), 
    path("add/", add_student_page, name="add_student"),
    path("edit/<int:id>/", edit_student_page, name="edit_student"),
    path('archive/', archive_page, name='archive'), 
    path('dashboard/', dashboard_page, name='dashboard'), 
    path('student/<int:id>', single_page, name='single'), 
]