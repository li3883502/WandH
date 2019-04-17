# -*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Category(models.Model):
    '''
    视频分类
    '''
    name = models.CharField(max_length=50, verbose_name=u'视频分类')
    number = models.IntegerField(default=0, verbose_name=u'分类数目')

    def __str__(self):  # 记得加上str,str中属性用self.xxx
        return self.name


class Tag(models.Model):
    '''
    视频标签
    '''
    name = models.CharField(max_length=10, verbose_name=u'视频标签')
    number = models.IntegerField(default=0, verbose_name=u'标签数量')

    def __str__(self):
        return self.name


class Video(models.Model):
    '''
    视频
    '''
    title = models.CharField(max_length=50, verbose_name=u'视频名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    message = models.TextField(verbose_name=u'相关信息', blank=True)
    image_url = models.CharField(max_length=200, verbose_name=u'封面地址', blank=True)
    score = models.FloatField(default=0.0, verbose_name=u'评分')
    intro = models.TextField(verbose_name=u'简介', blank=True)
    photo_url = models.TextField(verbose_name=u'剧照', blank=True)
    play_url = models.TextField(verbose_name=u'下载链接', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'分类')
    tag = models.ManyToManyField(Tag, verbose_name=u'标签')
    num = models.IntegerField(default=0, verbose_name=u'点击量')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.create_time >= timezone.now() - datetime.timedelta(days=7)


class Comment(models.Model):
    '''
    评论
    '''
    name = models.CharField(max_length=20, default=u'佚名', verbose_name=u'用户名')
    content = models.CharField(max_length=400)
    num = models.IntegerField(default=0, verbose_name=u'评论数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')
    blog = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name=u'视频')
    patent_comtents = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ':' + self.content

