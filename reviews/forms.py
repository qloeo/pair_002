from django import forms
from .models import Review, Comment, ReComment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image')
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ReCommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글')
    class Meta:
        model = ReComment
        fields = ('content',)