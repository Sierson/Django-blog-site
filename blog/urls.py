from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name="blog"),
    path('create-post/', views.CreatePost.as_view(), name="create_post"),
    path('post-detail/<slug:slug>', views.post_detail, name="post_detail")
]
