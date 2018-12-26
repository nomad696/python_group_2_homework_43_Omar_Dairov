"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import ArticleListView, ArticleDetailView, CreateArticleView, DeleteArticleView, UserListView, UserDetailView, UserCreateView, UserDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/create', CreateArticleView.as_view(), name='create_article'),
    path('article/<int:pk>/delete_article', DeleteArticleView.as_view(), name='remove_article'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/create', UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/delete_user', UserDeleteView.as_view(), name='user_delete')
]
