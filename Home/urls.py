from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'Home'

urlpatterns = [
    path('', views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(), name="user_login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("success/", views.form_success, name="success"),
    path("careers/", views.employeeApplication, name="employeeApplication"),
    path("services/", views.services, name='services'),
    path('services/', views.services, name='services_by_category'),
    path("services/<int:id>/<slug:slug>", views.service_detail, name="service_detail"),
    path("quote/", views.requestAQuote, name="requestAQuote"),
    path("aboutUs/", views.about_us, name="about_us"),
    path("viewGallery/<int:pk>", views.view_gallery, name="view_gallery"),
    path("ourProcess/", views.our_process, name="our_process"),

]
