from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Student


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["title", "content", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": CKEditorWidget(),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
