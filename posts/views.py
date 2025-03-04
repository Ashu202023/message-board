# from django.shortcuts import render
# from .models import Post

# def post_list(request):
#     p=Post.objects.all()
#     return render(request,"posts_list.html",{"posts":p})
# # Create your views here.
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model=Post
    template_name="posts_list.html"