from django.contrib import admin
from .models import categorydb
from .models import productdb
# Register your models here.

admin.site.register(categorydb)
admin.site.register(productdb)