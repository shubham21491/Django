from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_soft,name='All_home'),
    
]
