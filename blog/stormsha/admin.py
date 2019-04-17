from django.contrib import admin
from .models import Article, Tag, Category, Carousel, Keyword, FriendLink, Bigcategory
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')

    list_display_links = ('title',)

    list_filter = ('create_date', 'category')

    list_per_page = 50

    filter_horizontal = ('tags', 'keywords')

    


