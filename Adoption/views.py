from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Adoption.models import Adoptions
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Adoption(ListView):
    model = Adoptions
    template_name = 'Adoption/adoption.html'

class AdoptionDetails(DetailView):
    model = Adoptions
    template_name = 'Adoption/adoption_details.html'
