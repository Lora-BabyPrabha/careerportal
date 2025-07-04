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
