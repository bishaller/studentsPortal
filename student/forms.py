from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Student


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "content", "category"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "p-2 mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm text-lg border-gray-300 rounded-md"}),
            "content": CKEditorWidget(),
            "category": forms.Select(attrs={"class": "p-2 mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm text-lg border-gray-300 rounded-md"}),
        }
