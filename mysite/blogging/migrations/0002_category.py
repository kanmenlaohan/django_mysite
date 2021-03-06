# Generated by Django 2.2.5 on 2019-11-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('posts', models.ManyToManyField(blank=True, related_name='Category', to='blogging.Post')),
            ],
        ),
    ]
