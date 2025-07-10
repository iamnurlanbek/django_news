from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]

# MEDIA fayllar ishlashi uchun
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Agar local serverda STATIC_ROOT ishlatmoqchi bo'lsang:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
