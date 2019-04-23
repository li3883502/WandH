from django.shortcuts import render
from django.views import generic
from .models import Article, Bigcategory, Category, Tag
# Create your views here.


class IndexView(generic.ListView):
    model = Article
    template_name = 'stormsha/templates/index.html'
    context_object_name = 'articles'


class DetailView(generic.DetailView):
    '''
    用于显示一个对象的详情页.
    '''
    model = Article

    template_name = 'article.html'

    context_object_name = 'article'

    def get_object(self):
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(obj.id)
        

