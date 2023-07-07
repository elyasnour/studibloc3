from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from django.views.generic import ListView

from catalog.models import Product

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa


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
            Q(category__icontains=query) | Q(category__icontains=query)
        )


# Create your views here.
@login_required
def pdf_report_create(request):
    product_list = Product.objects.all()
    template_path = 'pdf/pdf_report.html'
    context = {'product_list': product_list, 'date': datetime.today()}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="liste_de_produit_en_promotion.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # creer le pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def product_discount(request):
    product_list = Product.objects.filter(discount__isnull=False)
    context = {'product_list': product_list, 'date': datetime.today() }
    return render(request, 'catalog/products_discount.html', context)
