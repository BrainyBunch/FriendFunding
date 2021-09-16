# Generated by Django 3.2.7 on 2021-09-15 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendfunding', '0007_auto_20210915_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='user',
        ),
        migrations.AddField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='friendfunding.user'),
        ),
    ]