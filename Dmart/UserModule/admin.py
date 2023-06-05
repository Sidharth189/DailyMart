from django.contrib import admin
from .models import contactdb
from .models import userdb,cartdb,shippingaddressdb

# Register your models here.

admin.site.register(contactdb)
admin.site.register(userdb)
admin.site.register(cartdb)
admin.site.register(shippingaddressdb)