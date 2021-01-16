from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=264, verbose_name="Title")
    slug = models.SlugField(max_length=264, unique=True)
    content = models.TextField(max_length=3000, verbose_name="Write your content here...")
    image = models.ImageField(upload_to='post_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    content = models.TextField(max_length=1000, verbose_name="Write your comment here...")
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.content

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")