from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views import generic, View
from .models import Post
from .forms import PostForm

class PostListView(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'add_post.html', context)


    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            slug = slugify(title)
            author = User.objects.get(username=request.user)
            post = Post.objects.create(title=title, slug=slug, content=content, author=author)
            return redirect('home')


class EditPostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {'form': form, 'post': post}
        return render(request, 'edit_post.html', context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.slug = slugify(form.cleaned_data['title'])
            post.save()
            return redirect('home')
