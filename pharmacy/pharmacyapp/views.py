from django.shortcuts import render
from .models import Factory, Drug
from django.db.models import Q


def home(request):
    drugs = Drug.objects.all().order_by('-price')
    return render(request, 'home.html', context={'drugs': drugs})

def search_drug(request):
    value = request.GET.get('drug_name')
    drugs = Drug.objects.filter(Q(title__icontains=value) | Q(factory__title__icontains=value))
    return render(request, 'home.html', context={'drugs': drugs})
   
