from django.db import models 


# Create your models here.
class Post(models.Model):
    title = models.CharField("제목", max_length=30,)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일시", auto_now_add=True) # auto_now_add : 처음 생성됐을 때
    updated_at = models.DateTimeField("글수정시간", auto_now=True) # auto_now : 게시글이 변경될때 마다

    def __str__(self):
        return f"[{self.id}] {self.title}"
    
    def get_absolute_url(self):
        return f"/blog/{self.pk}/"

