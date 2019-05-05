from django.db import models


# Create your models here.


class Friendly(models.Model):
    # 友情连接
    website = models.CharField(max_length=100)  # 网站名称
    url = models.URLField(max_length=200)  # 网站地址
    content = models.TextField()  # 网站服务内容

    def __str__(self):
        return self.content[:20]
