from django import forms
from .models import Post
from .models import Picture

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','public','summary','content','document_type']

class PictureForm(forms.ModelForm):

        class Meta:
            model = Picture
            fields = ['name','picture']