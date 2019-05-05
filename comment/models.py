from django.db import models
from blog.models import Post


# Create your models here.

class Comment(models.Model):
    # 评论
    name = models.CharField(max_length=52, blank=False)  # 昵称
    email = models.CharField(max_length=50)  # 邮箱
    content = models.TextField()  # 评论内容
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)  # 外键关联，标识评论文章

    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = [
            '-time'
        ]
