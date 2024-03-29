from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,'todo/post/index.html',{'posts':posts}) 

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,
                                  status='published',
                                  publish__year = year,
                                  publish__month = month,
                                  publish__day = day)
    return render(request,'todo/post/detail.html',{'post':posts})