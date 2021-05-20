from django.contrib import admin

# Register your models here.
from .models import Count

class CountAdmin(admin.ModelAdmin):
    search_fields = ('cnt',)
    list_display = ['cnt']

admin.site.register(Count,CountAdmin)