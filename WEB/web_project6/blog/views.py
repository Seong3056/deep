from django.shortcuts import render, redirect
from blog.models import Post
from django.views.generic import ListView

# Create your views here.
def index(request):
   '''
   FBV 방식 게시글 목록페이지
   '''
   posts = Post.objects.all().order_by("-pk")  # order_by(""): 순서 정렬하기
   context = {
       "posts" : posts,        
   }
   return render(request, "blog-list.html", context)
# class PostList(ListView):
#     model = Post
#     context_object_name = "posts"
    
#     template_name = "blog-list.html"

def single_post_page(request, post_id):
    blogid = Post.objects.get(id=post_id)
    posts = Post.objects.all()
    context = {
        "ID" : blogid,  # 키 값이 html이 받을 이름, value 가 전달될 데이터
        "POSTS" : posts,
    }
    return render(request,"single_post_page.html", context)


    