from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'rating']

class projectImageInline(admin.StackedInline):
    model = ProjectGallery
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'service']
    inlines = [
        projectImageInline
    ]
