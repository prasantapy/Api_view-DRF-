from django.db import models

# Create your models here.
class Job_Profile(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=12)
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Skill_CHOICES=[
        ('Py','python'),
        ('Java','Java')]
    skill=models.CharField(max_length=10,choices=Skill_CHOICES)

    Age=models.IntegerField()
    Email_id=models.EmailField(max_length=254)
