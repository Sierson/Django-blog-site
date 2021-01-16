from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from .forms import CommentForm, PostEditForm

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
'''
class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    template_name = 'blog/edit_post.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog:post_detail', kwargs={'slug':self.object.slug})
'''
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'slug':post.slug}))

    context = {'form': form}
    return render(request, 'blog/edit_post.html', context=context)

@login_required
def my_posts(request):
    user = User.objects.get(pk=request.user.pk)
    context = {'user': user}
    return render(request, 'blog/my_posts.html', context=context)



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    already_liked = ''
    try:
        already_liked = Like.objects.filter(post=post, user=request.user)
    except:
        pass

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)

        if form.is_valid():
            com_obj = form.save(commit=False)
            com_obj.user = request.user
            com_obj.post = post
            com_obj.save()

    context = {'post': post, 'form': form, 'already_liked': already_liked}

    return render(request, 'blog/post_detail.html', context=context)

@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    if not already_liked:
        liked_post = Like(post=post, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'slug':post.slug}))

@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'slug':post.slug}))
