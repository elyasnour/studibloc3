from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from studibloc3 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path("api/", include("apis.urls")), # new
    path("api-auth/", include("rest_framework.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
