from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.sign_up, name="sign_up"),
    path('signin/', views.sign_in, name="sign_in"),
    path('logout/', views.logoff, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('password/', views.change_password, name="change_password"),
    path('add-profile-picture/', views.add_profile_picture, name="add_profile_picture"),
    path('change-profile-picture/', views.change_profile_picture, name="change_profile_picture"),
]
