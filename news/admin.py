from django.contrib import admin
from news.models import *
from pyBSDate import bsdate

# Register your models here.

admin.site.site_header = "Jana Bechar Admin-Panel"
admin.site.site_title = "Jana Bechar"
admin.site.index_title = "Welcome to Jana Bechar"


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category',
                    'is_highlighted', 'is_main', 'bsDate', 'published_at']
    list_filter = ['category', 'is_highlighted', 'is_main']
    search_fields = ['title', 'category__name']
    list_per_page = 10
    list_editable = ['is_highlighted', 'is_main']

    def bsDate(self, obj):
        date = convert_AD_to_BS(obj.published_at.year,
                                obj.published_at.month, obj.published_at.day)
        ne_date = bsdate(date[0], date[1], date[2])
        return ne_date.strftime("%B %d %Y,%A", lang='ne')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)
admin.site.register(Subscription)
