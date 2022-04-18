# Generated by Django 4.0.2 on 2022-02-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_mainnews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainnews',
            name='new',
        ),
        migrations.AddField(
            model_name='mainnews',
            name='new',
            field=models.ManyToManyField(null=True, related_name='main_news', to='news.News'),
        ),
    ]