from django.contrib import admin
from django.utils.html import format_html

from catalog.models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "category", "price", "discount_rate")
    list_filter = ("name", "category",)
    search_fields = ("name", "category")


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("thumbnail_tag", "product_name")
    readonly_fields = ("thumbnail",)
    search_fields = ("product__name",)

    """cette fonction renvoie du HTML pour la première colonne définie
        dans la propriété list_display """

    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html('<img src="%s"/>' % obj.thumbnail.url)
        return "-"

    # ceci définit le nom de la colonne pour le list_display
    thumbnail_tag.short_description = "Thumbnail"

    def product_name(self, obj):
        return obj.product.name


admin.site.register(ProductImage, ProductImageAdmin)
