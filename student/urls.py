from django.urls import path
from .views import index_page, single_page, archive_page

urlpatterns = [
    path('', index_page, name='index'), 
    path('student/<int:id>', single_page, name='single'), 
    path('archive/', archive_page, name='archive'), 
]