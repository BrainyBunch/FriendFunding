# Generated by Django 3.2.7 on 2021-09-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendfunding', '0005_goal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='goal',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
