from django.urls import path,re_path
from .views import IndexView

app_name = 'stormsha'
urlpatterns = [
    # 首页
    re_path(r'^$', IndexView.as_view(template_name='stormsha/index.html'), name='index'),  # 主页，自然排序

    # 分类页面

    re_path(r'^category/(?P<bigslug>.*?)/(?P<slug>.*?)', IndexView.as_view(template_name='stormsha/content.html'), name='category'),
    # 归档页面
    # re_path(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', IndexView.as_view(template_name='archive.html'), name='date'),
    # # 标签页面
    # re_path(r'^tag/(?P<tag>.*?)/$', IndexView.as_view(template_name='content.html'), name='tag'),path('category',include(path('<bigslug>')IndexView.as_view(template_name='stormsha/content.html'), name='category')

    ]


