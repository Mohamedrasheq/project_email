from django.db import models

# Create your models here.
class register_details(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    exam=models.CharField(max_length=300)


class automate(models.Model):
    job_name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='pics', blank=True, null=True)
    desc=models.TextField()
    rules=models.TextField()
    