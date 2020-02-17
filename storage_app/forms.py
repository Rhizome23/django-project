from django import forms
from .models import Post, Picture
from ckeditor_uploader.widgets import  CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(required=False,widget=CKEditorUploadingWidget(config_name="custom_ckeditor"))

    class Meta:
        model = Post

        fields = ['title','public','summary','content']

class PictureForm(forms.ModelForm):

        class Meta:
            model = Picture
            fields = ['name','picture']