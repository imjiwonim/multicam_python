from django import forms
from board.models import Comment, Post

# Comment 모델을 기반으로 한 ModelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            # "user",
            "post",
            "content",]

# Post 모델을 기반으로 한 ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]