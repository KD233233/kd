# Generated by Django 2.1.7 on 2019-02-27 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190227_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readnum',
            old_name='read_num',
            new_name='look',
        ),
        migrations.RemoveField(
            model_name='post',
            name='look',
        ),
    ]