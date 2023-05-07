from django import forms
from .models import uploadimages


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = uploadimages
        fields = ['title', 'imageupload', 'description', 'category']
