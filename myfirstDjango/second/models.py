from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class secondary(models.Model):
    SoftwareType=[('M','Mac'),
                  ('L','Linux'),('W','Windows')]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='second/')
    date_Added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=1,choices=SoftwareType)
    description =models.TextField(max_length=100)
    def __str__(self):
        return self.name
# one to many  
class softwareReviews(models.Model):
    second = models.ForeignKey(secondary,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating =models.IntegerField()
    comment =models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username} review for {self.second.name}"
    

# many to many   
class store(models.Model):
    name = models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    second_variety = models.ManyToManyField(secondary,related_name='stores')
    def __str__(self):
        return self.name
    
# one to one

class secondCertify(models.Model):
    second =models.OneToOneField(secondary,on_delete=models.CASCADE,related_name='Certificate')
    certificate_number=models.CharField(max_length=100)
    issued_Date=models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()
    def __str__(self):
        return f"Certifiacte for {self.name.second}"


