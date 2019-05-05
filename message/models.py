from django.db import models

# Create your models here.

class Message(models.Model):
    # 留言
    name = models.CharField(max_length=52, blank=False)  # 昵称
    email = models.CharField(max_length=50)  # 邮箱
    content = models.TextField()  # 留言内容
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]


    class Meta:
        ordering = [
            '-time'
        ]
