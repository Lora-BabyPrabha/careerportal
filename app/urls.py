from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),

    # Admin dashboard and sections
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/home/', views.manage_home, name='manage_home'),
    path('dashboard/about/', views.manage_about, name='manage_about'),

    # Messages
    path('dashboard/messages/', views.view_messages, name='view_messages'),
    path('dashboard/messages/delete/<int:pk>/', views.delete_message, name='delete_message'),

    # Applications
    path('admin/applications/', views.view_applications, name='view_applications'),
    path('admin/applications/delete/<int:pk>/', views.delete_application, name='delete_application'),

    # Jobs
    path('admin/jobs/', views.manage_jobs, name='manage_jobs'),
    path('admin/jobs/add/', views.add_job, name='add_job'),
    path('admin/jobs/edit/<int:pk>/', views.edit_job, name='edit_job'),
    path('admin/jobs/delete/<int:pk>/', views.delete_job, name='delete_job'),
]




