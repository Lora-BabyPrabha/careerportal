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
from django.shortcuts import render, redirect, get_object_or_404
from .models import HomeContent, AboutPage, ContactMessage, JobApplication, JobDetails
from .forms import HomeContentForm, AboutPageForm, JobDetailsForm

def admin_dashboard(request):
    home = HomeContent.objects.first()
    about = AboutPage.objects.first()
    job_count = JobDetails.objects.count()
    app_count = JobApplication.objects.count()
    msg_count = ContactMessage.objects.count()
    return render(request, 'admin_dashboard.html', {
        'home': home,
        'about': about,
        'job_count': job_count,
        'app_count': app_count,
        'msg_count': msg_count
    })

def manage_home(request):
    home, _ = HomeContent.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = HomeContentForm(request.POST, instance=home)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = HomeContentForm(instance=home)
    return render(request, 'admin_manage_home.html', {'form': form})

def manage_about(request):
    about, _ = AboutPage.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AboutPageForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AboutPageForm(instance=about)
    return render(request, 'admin_manage_about.html', {'form': form})

def view_messages(request):
    messages = ContactMessage.objects.all().order_by('-submitted_at')
    return render(request, 'admin_messages.html', {'messages': messages})

def delete_message(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    message.delete()
    return redirect('view_messages')

def view_applications(request):
    applications = JobApplication.objects.all().order_by('-submitted_at')
    return render(request, 'admin_applications.html', {'applications': applications})

def delete_application(request, pk):
    app = get_object_or_404(JobApplication, pk=pk)
    app.delete()
    return redirect('view_applications')

def manage_jobs(request):
    jobs = JobDetails.objects.all()
    return render(request, 'admin_jobs.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        form = JobDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_jobs')
    else:
        form = JobDetailsForm()
    return render(request, 'admin_add_job.html', {'form': form})

def edit_job(request, pk):
    job = get_object_or_404(JobDetails, pk=pk)
    if request.method == 'POST':
        form = JobDetailsForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('manage_jobs')
    else:
        form = JobDetailsForm(instance=job)
    return render(request, 'admin_edit_job.html', {'form': form, 'job': job})

def delete_job(request, pk):
    job = get_object_or_404(JobDetails, pk=pk)
    job.delete()
    return redirect('manage_jobs')
