# Generated by Django 2.1.7 on 2019-02-23 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('classify', models.CharField(choices=[('网站前端', '网站前端'), ('后端技术', '后端技术')], max_length=20)),
                ('look', models.IntegerField(default=0)),
                ('zan', models.IntegerField(default=0)),
                ('adv', models.BooleanField(default=False, verbose_name='广告位')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
