from django.contrib import admin
from .models import People, Address, Doctor, Bio, Product

# Register your models here.

admin.site.register(People)
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Bio)
admin.site.register(Product)