from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('sign-up/', views.sign_up, name="sign_up")
]
