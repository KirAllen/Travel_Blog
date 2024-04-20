# Generated by Django 5.0.2 on 2024-04-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_remove_plan_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='plan',
            name='from_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='to_date',
            field=models.DateTimeField(),
        ),
    ]