from django.db import models
from django.utils import timezone
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