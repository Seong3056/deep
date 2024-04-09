from django import forms
from posts.models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",      
            "content",
        ]
        widgets = {        # widgets : 특수한 상황 작성시 사용
            "content": forms.Textarea(
                attrs={
                    "placeholder": "댓글 달기...",
                }
            )
        }

class PostForm(forms.ModelForm): # 모델과 관련된 form은 ModelForm 사용
    class Meta:   # Meta 모델과 form의 취급 방식을 변경할 때 사용
        model = Post
        fields = [
            "content",
        ]
        