from django.urls import path

from catalog import views
from catalog.views import ProductListView, SearchResultsListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),  # new
    path("discounts/", views.product_discount, name='discount'),
    path("pdf/", views.pdf_report_create, name='create-pdf'),  # new
]
