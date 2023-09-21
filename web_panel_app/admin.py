from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Category)
@admin.register(Company)
class ModelCategory(admin.ModelAdmin):
    list_display=['id']
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Volume)
admin.site.register(Cart)
# admin.site.register(Company)
admin.site.register(Testimonials)
admin.site.register(Contact_Us)
admin.site.register(AboutUs)
admin.site.register(Order)
admin.site.register(Address)