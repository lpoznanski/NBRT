from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views import generic, View
from .models import Post
from .forms import AddPostForm

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(View):
    def get(self, request):
        form = AddPostForm()
        context = {'form': form}
        return render(request, 'add_post.html', context)

    def post(self, request):
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            slug = slugify(title)
            author = User.objects.get(username=request.user)
            if 'add' in request.POST:
                post = Post.objects.create(title=title, slug=slug, content=content, status=1, author=author)
                return redirect('home')
            else:
                post = Post.objects.create(title=title, slug=slug, content=content, status=0, author=author)
                return redirect('home')

class EditPostView(View):
    pass
