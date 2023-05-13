from django.urls import path

from catalog.views import ProductListView, SearchResultsListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),  # new
]
