from django import forms
from .models import Post
from .models import FileDocument
from .models import Picture
from ckeditor_uploader.widgets import  CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(required=False,widget=CKEditorUploadingWidget())

    class Meta:
        model = Post

        fields = ['title','public','summary','content']

class FileDocumentForm(forms.ModelForm):

    class Meta:
        model = FileDocument
        fields = ['title','public','summary','content','document_type']


class PictureForm(forms.ModelForm):

        class Meta:
            model = Picture
            fields = ['name','picture']