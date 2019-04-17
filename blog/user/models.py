from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Ouser(AbstractUser):
    avatar = ProcessedImageField(upload_to='avatar/%Y/%m/%d', default='avatar/default.png', verbose_name='头像', processors=[ResizeToFill(90, 90)])

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

