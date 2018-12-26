from django import forms
from webapp.models import Article

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



# class DeleteArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['article']