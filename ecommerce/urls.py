from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('cart/', include('cart.urls')),
    path("", include("shop.urls")),
    path("__reload__/", include("django_browser_reload.urls")),  # !<- Dev dependency
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.TE_URL, document_root=settings.STATIC_ROOT)
