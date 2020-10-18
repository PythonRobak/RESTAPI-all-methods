from django.contrib import admin
from .models import Article

class ArticleDisplay(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'email', 'date_created', 'date_edited')
    search_fields = ('title', 'author', 'email')
    readonly_field = ('date_created', 'date_edited')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Article, ArticleDisplay)
