from django.contrib import admin
from webapp.models import Article, Issue, User, Commentary

# Register your models here.

admin.site.register(Article)
admin.site.register(Issue)
admin.site.register(User)
admin.site.register(Commentary)