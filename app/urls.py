from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import admin_dashboard 

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin_login.html'), name='admin_login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
]
