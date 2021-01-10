from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.account, name="account")
]
