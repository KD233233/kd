from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Sentence(models.Model):
    # 每日一句
    time = models.DateTimeField(auto_now=True)  # 时间
    content = models.TextField()  # 内容

    def __str__(self):
        return self.content


class Tags(models.Model):
    # 标签
    name = models.CharField(max_length=50)  # 标签名称

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    # 文章
    title = models.CharField(max_length=50)  # 标题
    content = models.TextField()  # 文章内容
    img = models.ImageField()  # 图片
    pub_time = models.DateTimeField(auto_now_add=True)  # 时间

    choices = (
        ('网站前端', '网站前端'),
        ('后端技术', '后端技术')

    )
    classify = models.CharField(max_length=20, choices=choices)  # 分类
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 作者
    tags = models.ManyToManyField(Tags)  # 标签
    # tags = models.ForeignKey(Tags, on_delete=models.DO_NOTHING)
    # look = models.IntegerField(default=0)  # 围观次数
    zan = models.IntegerField(default=0)  # 点赞量
    adv = models.BooleanField('广告位', default=False)  # 是否投放到广告位

    class Meta:
        ordering = [
            '-pub_time'
        ]

    def get_absolute_url(self):
        return reverse('content',kwargs={'id':self.pk})

    def read_num(self):
        try:
            return self.readnum.look
        except:
            return 0

    def __str__(self):

        return f'{self.id}'


class ReadNum(models.Model):
    look = models.IntegerField(default=0)
    post = models.OneToOneField(Post, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.look}'

class About(models.Model):
    # 关于博客页的内容
    content = models.TextField()
    qq = models.CharField(max_length=11)
    group = models.CharField(max_length=11)
    email = models.CharField(max_length=50)

