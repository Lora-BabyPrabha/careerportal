from django.shortcuts import render
from .models import HomeContent

def home(request):
    content = HomeContent.objects.first()  # Only one entry
    return render(request, 'home.html', {'content': content})

def jobs(request):
    return render(request, 'jobs.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
