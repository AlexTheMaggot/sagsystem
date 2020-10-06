from django.shortcuts import render, redirect
from .models import Incidents
from mainapp.models import Workers, Departments


def incidents_dashboard(request):
    if request.user.is_authenticated:
        incidents = Incidents.objects.filter(adder__exact=request.user)
        workers = Workers.objects.all()
        departments = Departments.objects.all()
        context = {
            'incidents': incidents,
            'workers': workers,
            'departments': departments
        }
        return render(request, 'incidents/incidents.html', context)
    else:
        return redirect('auth', permanent=True)


def incidents_add(request):
    if request.user.is_authenticated:
        return render(request, 'incidents/incidents_add.html')
    else:
        return redirect('auth', permanent=True)
