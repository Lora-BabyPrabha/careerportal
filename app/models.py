from django.db import models

class HomeContent(models.Model):
    headline = models.CharField(max_length=200)
    subheadline = models.TextField()
    
    stat_positions = models.CharField(max_length=100)
    stat_companies = models.CharField(max_length=100)
    stat_success = models.CharField(max_length=100)
    stat_salary = models.CharField(max_length=100)

    why_choose_us_title = models.CharField(max_length=100, default="Why Choose Us?")
    
    feature_1_title = models.CharField(max_length=100)
    feature_1_description = models.TextField()
    
    feature_2_title = models.CharField(max_length=100)
    feature_2_description = models.TextField()
    
    feature_3_title = models.CharField(max_length=100)
    feature_3_description = models.TextField()
    
    feature_4_title = models.CharField(max_length=100)
    feature_4_description = models.TextField()

    cta_title = models.CharField(max_length=200)
    cta_description = models.TextField()

    def __str__(self):
        return "Home Page Content"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    tagline = models.CharField(max_length=300, blank=True, null=True)
    who_we_are = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    core_values = models.TextField()

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class JobDetails(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, default="Full-time")  # Ensure this exists!
    description = models.TextField()
    requirements = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    benefits = models.TextField(blank=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
from django.db import models

class AboutContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    section_1_title = models.CharField(max_length=100)
    section_1_body = models.TextField()
    section_2_title = models.CharField(max_length=100)
    section_2_body = models.TextField()
    core_values = models.TextField(help_text="Separate values with commas")

    def __str__(self):
        return self.title
