from django.contrib import admin
from tab.models import Sale


class SaleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sale, SaleAdmin)
