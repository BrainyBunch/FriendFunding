# Generated by Django 3.2.7 on 2021-09-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendfunding', '0004_auto_20210912_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='title',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
