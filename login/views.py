from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(request):
    form = UserCreationForm()
    registered = False

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True

    context = {'form': form, 'registered': registered}
    return render(request, 'login/sign_up.html', context=context)