from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.

def index(request):
    return render(request,"index.html")

def post_list(request):
    POSTS = Post.objects.all()

    # 템플릿에 전달할 딕셔너리
    context = {
        "POSTS" : POSTS,
    }
    return render(request,"post_list.html", context) 

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id 값인 Post객체
    # print(post) # 가져온 객체를 print 함수로 확인
    if request.method == "POST":   # textarea의 name 속성값(comment)을 가져옴
        comment_content = request.POST["comment"]
        
        # 전달된 comment 값으로 Comment 객체를 생성
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
        # 1. GET 요청으로 글 상세 페이지를 보여주거나
        # 2. POST 요청으로 댓글이 생성되거나
        # 3. 두 경우 모두, 이 글의 상세 페이지를 보여주면 됨

    context = {
        "post" : post
    }

    return render(request, "post_detail.html", context) 
    
def post_add(request):
    if request.method == "POST": # method가 POST일 때        
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES.get("thumbnail", None) # 이미지 파일

        post = Post.objects.create(
            title=title,       # 우측 title은 if 문에 나오는 title 좌측은 models에 나오는 title
            content=content,
            thumbnail=thumbnail, # 이미지 파일을 게시글 객체 생성시에 전달
        )
        return redirect(f"/posts/{post.id}/")
                 
   # else: # method가 POST가 아닐 때
        # print("method GET")
        # print(request.POST) # POST 메서드로 전달된 데이터를 출력
    return render(request, "post_add.html")



