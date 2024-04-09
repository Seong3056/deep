from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("posts/", views.post_list, name="post_list.html"), # name = "" -> 변수명 같은거
    path("posts/<int:post_id>/", views.post_detail),
    path("posts/add/", views.post_add, name="post_add.html"),
]