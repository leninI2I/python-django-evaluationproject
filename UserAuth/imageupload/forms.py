from django import forms
from .models import uploadimages

# class ImageForm(forms.Form):
#     title = forms.CharField(max_length=100, label="Image Title")
#     description = forms.CharField(max_length=500, label="Image Description")
#     imageupload = forms.ImageField(required=True)
#     category = forms.CharField(max_length=50, label="Image category")

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = uploadimages
        fields = ['title', 'imageupload', 'description', 'category']
