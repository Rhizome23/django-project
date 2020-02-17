from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    summary = models.TextField(blank=True, max_length=1000)
    content = RichTextUploadingField(config_name="custom_ckeditor")
    def __str__(self):
        return self.title

class Picture(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    picture = models.ImageField(upload_to = 'media/')
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)



