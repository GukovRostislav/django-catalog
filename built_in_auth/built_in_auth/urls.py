from django.contrib import admin
from django.urls import include, path
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth2.urls')),
    path('', include('django.contrib.auth.urls'), name='login'),
    #path('', include(''), name='logout'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
