from django.shortcuts import render, redirect, get_object_or_404
from .models import HomeContent, ContactMessage, AboutPage, Job, JobApplication, JobDetails
from .forms import ContactForm, JobApplicationForm
from django.contrib import messages

def home(request):
    content = HomeContent.objects.first()  # Only one entry
    return render(request, 'home.html', {'content': content})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')  # name of the URL pattern
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render
from .models import JobDetails as Job  # or use your model directly

def jobs(request):
    jobs = Job.objects.all().order_by('-id')  # show latest jobs first

    search_query = request.GET.get('search', '')
    department = request.GET.get('department', '')
    job_type = request.GET.get('type', '')
    location = request.GET.get('location', '')

    if search_query:
        jobs = jobs.filter(title__icontains=search_query)

    if department:
        jobs = jobs.filter(department__iexact=department)

    if job_type:
        jobs = jobs.filter(job_type__iexact=job_type)

    if location:
        jobs = jobs.filter(location__iexact=location)

    context = {
        'jobs': jobs,
        'request': request  # used for filter form retention
    }
    return render(request, 'jobs.html', context)


def about(request):
    about_content = AboutPage.objects.first()  # get the first and only record
    return render(request, 'about.html', {'about': about_content})

def job_detail(request, job_id):
    job = get_object_or_404(JobDetails, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'job_application_success.html', {'job': job})
    else:
        form = JobApplicationForm()

    return render(request, 'job-details.html', {'job': job, 'form': form})

# views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import JobDetails, JobApplication

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    jobs = JobDetails.objects.all()
    applications = JobApplication.objects.all()
    return render(request, 'admin_dashboard.html', {
        'jobs': jobs,
        'applications': applications,
    })
