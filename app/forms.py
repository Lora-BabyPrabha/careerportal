from django import forms
from .models import HomeContent, AboutPage, ContactMessage, Job, JobDetails, JobApplication

class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = '__all__'

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobDetails
        fields = '__all__'
from django import forms
from .models import ContactMessage, JobApplication

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job', 'full_name', 'email', 'phone', 'cover_letter', 'resume']


from django import forms
from .models import JobDetails

class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobDetails
        fields = '__all__'


