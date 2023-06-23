from django import forms
from django.db.models.base import Model
from django.forms.models import ModelForm
from Home.models import Service, ServiceImage, ServicePromotion
from .models import Testimonial, ProjectGallery, Project

class AddService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'details', )

class AddTestimonial(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('quote', 'reviewer', 'rating')

class EditTestimonial(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('quote', 'reviewer', 'rating')

class EditService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'details',)

class EditThumbnail(forms.ModelForm):
    class Meta:
        model = ServiceImage
        fields = ('image', )

class AddImage(forms.ModelForm):
    class Meta:
        model = ServiceImage
        fields = ('image', )

class AddPromotion(forms.ModelForm):
    class Meta:
        model = ServicePromotion
        fields = ('image', )

class CreateGallery(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'thumbnail')

class AddGalleryImage(forms.ModelForm):
    class Meta:
        model = ProjectGallery
        fields = ('image', )

class EditProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'service', 'thumbnail')
