# Generated by Django 5.0.2 on 2024-04-16 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_alter_article_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Articles',
        ),
    ]