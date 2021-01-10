from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_more_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_more_info")
    profile_pic = models.ImageField(upload_to="profile_pics")
