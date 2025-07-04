from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
]
