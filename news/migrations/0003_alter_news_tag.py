# Generated by Django 4.0 on 2021-12-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_news_description_news_body_remove_news_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(blank=True, to='news.Tag'),
        ),
    ]
