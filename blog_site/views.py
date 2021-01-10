from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect(reverse('blog:blog'))