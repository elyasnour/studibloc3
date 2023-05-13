from django.urls import path

from catalog.views import ProductListView, AboutPageView, SearchResultsListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("search/", SearchResultsListView.as_view(), name="search_results"),  # new
]
