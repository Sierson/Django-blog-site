from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, EditProfileForm, ChangeProfileImageForm

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False

    if request.method == "POST":
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True

    context = {'form': form, 'registered': registered}
    return render(request, 'login/sign_up.html', context=context)

def sign_in(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:blog'))

    context = {'form': form}
    return render(request, 'login/sign_in.html', context=context)

@login_required
def logoff(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:blog'))

@login_required
def profile(request):
    context = {}
    return render(request, 'login/profile.html', context=context)

@login_required
def edit_profile(request):
    current_user = request.user
    form = EditProfileForm(instance=current_user)

    if request.method == "POST":
        form = EditProfileForm(data=request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))

    context = {'form': form}
    return render(request, 'login/edit_profile.html', context=context)

@login_required
def change_password(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)

    change = False

    if request.method == "POST":
        form = PasswordChangeForm(current_user, data=request.POST)

        if form.is_valid():
            form.save()
            change = True

    context = {'form': form, 'change': change}
    return render(request, 'login/change_password.html', context=context)

@login_required
def add_profile_picture(request):
    form = ChangeProfileImageForm()

    if request.method == "POST":
        form = ChangeProfileImageForm(request.POST, request.FILES)

        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('login:profile'))

    context = {'form': form}
    return render(request, 'login/change_profile_picture.html', context=context)

@login_required
def change_profile_picture(request):
    form = ChangeProfileImageForm(instance=request.user.user_more_info)

    if request.method == "POST":
        form = ChangeProfileImageForm(request.POST, request.FILES, instance=request.user.user_more_info)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))

    context = {'form': form}
    return render(request, 'login/change_profile_picture.html', context=context)