

from django.urls.conf import path
from news.views import *


urlpatterns = [

    path('', home, name='home'),
    path("<int:id>/", news, name="news"),
    path("category/<str:title>/", category, name="category"),
    path("search/", search, name="search"),
    path("tag/<str:name>/", tag, name="tag"),
    path("subsription/", subscription, name='subscription'),

    path("catagoryapi/", Catagorylist.as_view(), name='catagoryapi'),
    path("catagorybyid/<int:id>", Catagorybyid.as_view(), name='catagorybyidapi'),
    path("tagapi/", Taglist.as_view(), name='tagapi'),
    path("newsapi/", Newslist.as_view(), name='newsapi'),
    path("subscriptionapi/", Subscriptionlist.as_view(), name='subscriptionapi'),




]
