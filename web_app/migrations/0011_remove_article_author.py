# Generated by Django 5.0.2 on 2024-04-19 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0010_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
