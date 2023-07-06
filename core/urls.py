
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static, serve
from django.conf import settings

urlpatterns = [
    path('jbadmin/', admin.site.urls),
    path('', include('news.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    staticpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

else:
    staticpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += staticpatterns
