from django.shortcuts import render
from .models import DataBu


def index(request):
    queryset = DataBu.objects.all()
    context = {'queryset': queryset}
    return render (request, 'index.html', context)

def home(request):
    return render (request, 'home.html')
