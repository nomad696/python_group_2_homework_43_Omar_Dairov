from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from webapp.models import Article, User, Comment, Issue
from webapp.forms import ArticleForm, UserForm, CommentForm, IssueForm
from django.shortcuts import get_object_or_404, redirect


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class CreateArticleView(CreateView):
    model = Article
    template_name = 'create_article.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={ 'pk': self.object.pk})

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('article_list')

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.article.pk})

class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue_create.html'
    form_class = IssueForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.article.pk})

def favourite_article(request, user_id, article_id):
    user = User.objects.get(pk=user_id)
    article = get_object_or_404(Article, pk=article_id)
    user.favourite.add(article)
    user.save()
    return redirect('user_detail', pk=user_id)