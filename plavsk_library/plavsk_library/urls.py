from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('админ/', admin.site.urls),
    path('', include('main.urls')),
    path('основные-сведения', include('info.urls')),
    path('структура-организации', include('structure.urls')),
    path('история', include('history.urls')),
    path('услуги', include('services.urls')),
    path('новости', include('news.urls')),
    path('галерея', include('gallery.urls')),
    path('документы', include('documents.urls')),
    path('календарь-знаменательных-дат', include('dates.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import socket
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
