from django.contrib import admin
from marketing.models import Sales

class SalesAdmin(admin.ModelAdmin):
    list_display = ('sales_id','status','target',)

admin.site.register(Sales,SalesAdmin)
