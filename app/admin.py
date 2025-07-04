from django.contrib import admin
from .models import HomeContent, ContactMessage, AboutPage, JobDetails, JobApplication 

admin.site.register(HomeContent)
admin.site.register(ContactMessage)

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(JobDetails)
class JobDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'experience', 'job_type']
    list_filter = ['location', 'experience', 'job_type']
    search_fields = ['title', 'location', 'description']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'job', 'submitted_at']
    list_filter = ['job', 'submitted_at']
    search_fields = ['full_name', 'email', 'phone', 'job__title']