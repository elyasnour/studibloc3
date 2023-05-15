from django.db.models import Q
from django.views.generic import ListView, TemplateView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class SearchResultsListView(ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "catalog/search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        return Product.objects.filter(
            Q(category__icontains=query) | Q(name__icontains=query)
        )

