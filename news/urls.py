

from django.urls.conf import path
from news.views import *


urlpatterns = [

    path('', home, name='home'),
    path("<int:id>/", news, name="news"),
    path("category/<str:title>/", category, name="category"),
    path("search/", search, name="search"),
    path("tag/<str:name>/", tag, name="tag"),
    path("subsription/", subscription, name='subscription')



]
