from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "created_at",
        "updated_at",
    ]

# admin.site.register(Post) <- 관리자 페이지에 등록만 할거면 이방법으로 해도 됨