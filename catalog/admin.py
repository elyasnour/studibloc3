from django.contrib import admin

from catalog.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "category", "price")
    list_filter = ("name", "category",)
    search_fields = ("name", "category")


admin.site.register(Product, ProductAdmin)