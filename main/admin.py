

from django.contrib import admin
from .models import Product, Tag,  Review

admin.site.register(Product)
admin.site.register(Tag)

admin.site.register(Review)
# Register your models here.
