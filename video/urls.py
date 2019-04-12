from django.urls import path
from . import views

app_name = 'video'  # 建议使用app_name
urlpatterns = [  # 注意使用的是 [] 非 {}
    path('', views.index, name='index'),
    path('detail/<int:video_id>', views.detail, name='detail'),

]