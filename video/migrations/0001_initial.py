# Generated by Django 3.0 on 2019-04-10 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='视频分类')),
                ('number', models.IntegerField(default=0, verbose_name='分类数目')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='视频标签')),
                ('number', models.IntegerField(default=0, verbose_name='标签数量')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateField(auto_now=True)),
                ('message', models.TextField()),
                ('image_url', models.URLField()),
                ('score', models.FloatField(default=0.0)),
                ('intro', models.TextField(verbose_name='')),
                ('photo_url', models.TextField(verbose_name='剧照')),
                ('play_url', models.TextField(verbose_name='下载链接')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Category')),
                ('tags', models.ManyToManyField(to='video.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='佚名', max_length=20, verbose_name='用户名')),
                ('content', models.CharField(max_length=400)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='视频')),
                ('patent_comtents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Comment')),
            ],
        ),
    ]