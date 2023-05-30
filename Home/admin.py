from django.contrib import admin
from .models import *

# Register your models here.

class serviceImageInline(admin.StackedInline):
    model = ServiceImage
    extra = 0

class promotionalImageInline(admin.StackedInline):
    model = ServicePromotion
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug': ('name', )}
    inlines = [
        serviceImageInline, promotionalImageInline
    ]

@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['service']

@admin.register(requestAQuote)
class quoteAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Employee)
class employeeAdmiin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
