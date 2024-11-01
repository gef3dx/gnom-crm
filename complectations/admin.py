from django.contrib import admin
from .models import (
    Complectation,
    Product,
    GroupProduct,
    Provider,
    Receipts
)

admin.site.register(Complectation)
admin.site.register(Product)
admin.site.register(GroupProduct)
admin.site.register(Provider)
admin.site.register(Receipts)


