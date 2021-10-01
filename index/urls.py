from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.aboutus,name='about'),
    path('team/',views.team,name='team'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('services/',views.services,name='services'),
    path('deceased/',views.deceased,name='deceased'),
    path('carcass/',views.carcass,name='carcass'),
    path('ceremony/',views.ceremony,name='ceremony'),
    path('memorabilia/',views.memorabilia,name='memorabilia'),
    path('termsofservice/',views.termsofservice,name='termsofservice'),
    path('privacypolicy/',views.privacypolicy,name='privacypolicy'),
]
