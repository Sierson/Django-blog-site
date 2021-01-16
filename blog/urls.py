from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name="blog"),
    path('create-post/', views.CreatePost.as_view(), name="create_post"),
    path('my-post/', views.my_posts, name="my_posts"),
    path('post-detail/<slug:slug>', views.post_detail, name="post_detail"),
    path('post-edit/<pk>', views.edit_post, name="edit_post"),
    path('liked/<int:pk>/', views.liked, name="liked_post"),
    path('unliked/<int:pk>/', views.unliked, name="unliked_post"),
]
