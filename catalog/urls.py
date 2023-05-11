from django.urls import path

from catalog.views import ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
]
