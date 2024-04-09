from django.shortcuts import render, redirect

def index(request):
    # 로그인이 된 경우 feeds페이지로
    if request.user.is_authenticated:
        return redirect("posts:feeds")   # redirect 다른페이지로 보내버린다는 의미
    # 아닐경우 login 페이지로
    else:
        return redirect("users:login")
    
