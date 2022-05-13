

from datetime import date, datetime
from operator import ge
from pyexpat import model
from django.db import models
from pyBSDate import convert_BS_to_AD
from pyBSDate import convert_AD_to_BS
from pyBSDate import bsdate
from django.db.models.deletion import SET_NULL
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def get_obs_upload_path():
    today = datetime.now()

    # this will create something like "2011/08/30"
    today_path = today.strftime("%Y/%m/%d")
    path = str(today_path)

    return path


class News(models.Model):
    title = models.CharField(max_length=500)
    is_highlighted = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='cat')
    tag = models.ManyToManyField(
        Tag, blank=True, related_name='tag')
    description = models.TextField(blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=get_obs_upload_path())
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    @property
    def bsDate(self):
        date = convert_AD_to_BS(self.published_at.year,
                                self.published_at.month, self.published_at.day)
        ne_date = bsdate(date[0], date[1], date[2])
        return ne_date.strftime("%B %d %Y,%A", lang='ne')


class Subscription(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email
