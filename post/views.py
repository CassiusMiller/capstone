from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
)
from .models import Post
# Create your views here.
class PostListView(ListView):
  template_name = 'post/post_list.html'
  model = Post
  context_object_name = 'posts'
class PostDetailView(DetailView):
  template_name = 'post/post_detail.html'
  model = Post
  context_object_name = 'post'
class PostCreateView(CreateView):
  template_name = 'post/post_create.html'
  model = Post
  fields = ['title', 'content']
  success_url = '/posts/'  # Redirect to the post list after creation

  def form_valid(self, form):
    form.instance.author = self.request.user  # Set the author to the current user
    return super().form_valid(form)