from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),  # ✅ Add this
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
