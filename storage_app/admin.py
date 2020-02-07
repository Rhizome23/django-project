from django.contrib import admin
from .models import Post, PrivatePost
from django.db import models

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on"]
    list_display_links = ["title"]


admin.site.register(Post,PostModelAdmin)

