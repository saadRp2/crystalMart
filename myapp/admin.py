from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(user)
admin.site.register(product)
admin.site.register(main_category)
admin.site.register(branding)
admin.site.register(prize)
admin.site.register(color)
admin.site.register(size)
# admin.site.register(coupon)
admin.site.register(billing)
admin.site.register(wishlist)
