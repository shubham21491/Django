from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_soft,name='All_home'),
    path('<int:second_id>/',views.second_Details,name='second_details'),
    
]
