from django.shortcuts import render
from .models import secondary
from django.shortcuts import get_object_or_404
# Create your views here.
def all_soft(request):
    seconds=secondary.objects.all()
    return render(request,'second/all_second.html',{'seconds':seconds})

def second_Details(request,second_id):
    second=get_object_or_404(secondary,pk=second_id)
    return render(request,'second/second_details.html',{'second':second})