# Generated by Django 2.1.7 on 2019-02-23 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
