from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc')
    search_fields = ('name',)
    list_editable = ('price', 'desc')
    actions = ('set_price_to_zero',)

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)

admin.site.site_header = "Perry's Home Admin"
admin.site.index_title = "Manage Perry's Home"
admin.site.site_title = "Perry Home"
