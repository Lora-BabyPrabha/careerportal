from django.contrib import admin
from .models import HomeContent, ContactMessage, AboutPage, JobDetails

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


