from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on"]
    list_display_links = ["title"]

admin.site.register(Post,PostModelAdmin)

