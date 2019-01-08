from django import forms
from webapp.models import Article, User, Comment, Issue

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('article', 'description', 'user')


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('article', 'description', 'user')

        def get_create(self):
            return Article('article_detail', kwargs={'pk':self.pk})

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email')

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email')

        def get_create(self):
            return User('user_detail', kwargs={'pk':self.pk})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'article', 'user']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['article', 'user', 'status']