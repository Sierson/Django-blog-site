from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView
from .models import Post, Comment, Like
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Post
    template_name = 'blog/blog.html'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ('title', 'content', 'image')

    def form_valid(self, form):
        post_obj = form.save(commit=False)
        post_obj.author = self.request.user
        title = post_obj.title
        post_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        post_obj.save()
        return HttpResponseRedirect(reverse('index'))

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}

    return render(request, 'blog/post_detail.html', context=context)