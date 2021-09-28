from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.aboutus,name='about'),
    path('team/',views.team,name='team'),
    path('testimonials/',views.testimonials,name='testimonials'),
]
