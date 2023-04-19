from django.shortcuts import render
from .models import Thing, UoM

def thinglist(request):
    thinglst = Thing.objects.all()
    return render(request, 'thingctlg/thinglst.html', {'thinglst': thinglst})


def uomlist(request):
    uomlst = UoM.objects.all()
    return render(request, 'thingctlg/uomlst.html', {'uomlst': uomlst})