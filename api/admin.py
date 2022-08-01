from django.contrib import admin
from .models import Upcoming, Orders, Ratings, Comments

# Register your models here.

# admin.site.register(Upcoming)

# @admin.register(Upcoming)
# class UpcomingModel(admin.ModelAdmin):
#     list_filter = ('resturant_name', 'date', 'time')
#     list_display = ('resturant_name', 'date', 'time')

admin.site.register(Upcoming)
admin.site.register(Orders)
admin.site.register(Ratings)
admin.site.register(Comments)

