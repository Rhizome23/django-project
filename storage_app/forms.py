from django import forms
from .models import Post
from .models import Picture
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    summary= forms.CharField(required=False,
                      widget=TinyMCEWidget(attrs={'placeholder': 'Enter description'}), max_length=100)
    class Meta:
        model = Post

        fields = ['title','public','summary','content','document_type']


class PictureForm(forms.ModelForm):

        class Meta:
            model = Picture
            fields = ['name','picture']