from django.urls import path
from storage_app import views

urlpatterns = [
        path('', views.home_page, name='home'),
        path("all_posts/", views.all_posts, name="all_posts"),
        path("all_pictures/", views.all_pictures, name="all_pictures"),
        path("public_posts/", views.public_posts, name="public_posts"),
        path('delete/<uuid:uuid>/', views.delete, name='delete'),
        path('delete_picture/<uuid:uuid>/', views.delete_picture, name='delete_picture'),
        path('edit_picture/<uuid:uuid>/', views.edit_picture, name='edit_picture'),
        path('edit/<uuid:uuid>/', views.edit, name='edit'),
        path("post_detail/<uuid:uuid>/", views.post_detail, name="post_detail"),
        path("picture_detail/<uuid:uuid>/", views.picture_detail, name="picture_detail"),
        path('post_form', views.post_form, name='post_form'),
        path('picture_form', views.picture_form, name='picture_form'),

]
