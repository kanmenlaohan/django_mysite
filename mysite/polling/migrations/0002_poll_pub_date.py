# Generated by Django 2.2.5 on 2019-11-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default='2000-1-1', verbose_name='date published'),
        ),
    ]
