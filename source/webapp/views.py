from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from webapp.models import Article
from webapp.forms import ArticleForm



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
