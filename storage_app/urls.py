from django.urls import path, include
from storage_app import views

urlpatterns = [
        path('', views.home_page, name='home'),
        path("all_posts/", views.all_posts, name="all_posts"),
        path("all_pictures/", views.all_pictures, name="all_pictures"),
        path("all_file_documents/", views.all_file_documents, name="all_file_documents"),
        path("public_posts/", views.public_posts, name="public_posts"),
        path('delete/<uuid:uuid>/', views.delete, name='delete'),
        path('delete_picture/<uuid:uuid>/', views.delete_picture, name='delete_picture'),
        path('delete_file_document/<uuid:uuid>/', views.delete_file_document, name='delete_file_document'),
        path('edit_picture/<uuid:uuid>/', views.edit_picture, name='edit_picture'),
        path('edit/<uuid:uuid>/', views.edit, name='edit'),
        path('edit_file_document/<uuid:uuid>/', views.edit_file_document, name='edit_file_document'),
        path("post_detail/<uuid:uuid>/", views.post_detail, name="post_detail"),
        path("file_document_detail/<uuid:uuid>/", views.file_document_detail, name="file_document_detail"),
        path("picture_detail/<uuid:uuid>/", views.picture_detail, name="picture_detail"),
        path('post_form', views.post_form, name='post_form'),
        path('picture_form', views.picture_form, name='picture_form'),
        path('file_document_form', views.file_document_form, name='file_document_form'),

]
