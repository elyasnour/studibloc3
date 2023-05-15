from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path("v1/", ProductAPIView.as_view(), name="product_list"),
    path("v1/<int:pk>", ProductDetailAPIView.as_view(), name="Product_detail"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"), # new
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",), # new
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"), # new
]
