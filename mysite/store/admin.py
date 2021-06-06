from django.contrib import admin
from .models import Shop,Category,Product,Blog,Brands,\
    Billing_Address,Regular,Order,Mini_Category,Sale

admin.site.register(Shop)
admin.site.register(Regular)
admin.site.register(Category)
admin.site.register(Mini_Category)
admin.site.register(Blog)
admin.site.register(Brands)
admin.site.register(Billing_Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Sale)