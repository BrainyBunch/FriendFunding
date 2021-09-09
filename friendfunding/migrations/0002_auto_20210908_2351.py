# Generated by Django 3.2.7 on 2021-09-08 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('friendfunding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='photo_url',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='album',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nationality',
        ),
        migrations.AddField(
            model_name='goal',
            name='amountsaved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='goal',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='goal',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='amountsaved',
            field=models.IntegerField(default=0),
        ),
    ]