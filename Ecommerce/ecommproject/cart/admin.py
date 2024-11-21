from django.contrib import admin
from cart.models import CartItem
from cart.models import Cart

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)