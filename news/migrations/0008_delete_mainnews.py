# Generated by Django 4.0.2 on 2022-02-11 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_is_highlighted_news_is_main'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MainNews',
        ),
    ]