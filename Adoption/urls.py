from django.urls import path
from . import views

app_name = 'Adoption'

urlpatterns=[
    path('', views.Adoption.as_view(), name='adoption'),
    path('adoption/<pk>/', views.AdoptionDetails.as_view(), name='adoption_details'),
]
