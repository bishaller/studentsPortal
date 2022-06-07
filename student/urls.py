from django.urls import path
from .views import index_page, single_page

urlpatterns = [
    path('', index_page, name='index'), 
    path('student/<int:id>', single_page, name='single'), 
]