from django.contrib import admin
from webapp.models import Article, Issue, User, Comment

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('favorites',)

admin.site.register(Article)
admin.site.register(Issue)
admin.site.register(User)
admin.site.register(Comment)