from django.shortcuts import render
from .models import secondary
# Create your views here.
def all_soft(request):
    seconds=secondary.objects.all()
    return render(request,'second/all_second.html',{'seconds':seconds})