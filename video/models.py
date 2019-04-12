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


class Tags(models.Model):
    '''
    视频标签
    '''
    name = models.CharField(max_length=50,verbose_name=u'视频标签')
    number = models.IntegerField(default=0,verbose_name=u'标签数量')

class Video(models.Model):
    '''
    视频
    '''
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateField(auto_now=True)
    message = models.TextField()
    image_url = models.URLField()
    score = models.FloatField(default=0.0)
    intro = models.TextField(verbose_name=u'')
    photo_url = models.TextField(verbose_name=u'剧照')
    play_url = models.TextField(verbose_name=u'下载链接')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return timezone.now() - self.modify_time <= datetime.timedelta(days=7)


class Comment(models.Model):
    '''
    评论
    '''
    name = models.CharField(max_length=20, default=u'佚名',verbose_name=u'用户名')
    content = models.CharField(max_length=400)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')
    blog = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name=u'视频')
    patent_comtents = models.ForeignKey('self', on_delete=models.CASCADE)

