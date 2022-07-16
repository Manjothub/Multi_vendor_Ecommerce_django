from django.contrib import admin
from .models import *

class Product_Image(admin.TabularInline):
    model = ProductImage

class Additional_Information(admin.TabularInline):
    model = AdditionalInformation

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Image,Additional_Information)
    list_display = ('product_name','price','categories','section')
    list_editable = ('categories','section')
    

admin.site.register(FrontSlider)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(ProductImage)
admin.site.register(AdditionalInformation)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CouponCode)