from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'Admin'

urlpatterns = [
    path('myConsole/', views.admin, name="admin"),
    path('quotes/', views.view_quotes, name="view_quotes"),
    path('deleteQuote/<int:id>', views.delete_quote, name="delete_quote"),
    path('myServices/', views.view_services, name="view_services"),
    path('editService/<int:pk>', views.edit_service, name='edit_service'),
    path('deleteService/<int:pk>', views.deleteService, name='deleteService'),
    path('editImages/<int:pk>', views.edit_service_images, name="edit_service_images"),
    path('deleteImage/<int:pk>', views.deleteServiceImage, name='deleteServiceImage'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('deleteTestimonial/<int:pk>', views.delete_testimonial, name='delete_testimonial'),
    path('applicants/', views.applicants, name='applicants'),
    path('applicant_details/<int:pk>', views.view_applicant_details, name="view_applicant_details"),
    path('deleteApplicant/<int:pk>', views.deleteApplicant, name="deleteApplicant"),
    path('editPromotions/<int:pk>', views.editPromotionalBanner, name="editPromotionalBanner"),
    path('deletePromotion/<int:pk>', views.deletePromotion, name="deletePromotion"),
    path('editGallery/<int:pk>', views.edit_gallery, name="edit_gallery"),
    path('deleteGalleryImage/<int:pk>', views.deleteGalleryImage, name="deleteGalleryImage"),
    path('deleteProject/<int:pk>', views.deleteProject, name='deleteProject'),
    path('createGallery/<int:pk>', views.createGallery, name="createGallery"),
    path('editProject/<int:pk>', views.edit_project, name="edit_project"),
    path('editTestimonial/<int:pk>', views.edit_testimonial, name="edit_testimonial"),

]
