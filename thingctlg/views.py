from django.shortcuts import render
from .models import Thing

def thinglist(request):
    thinglst = Thing.objects.all()
    return render(request, 'thingctlg/thinglst.html', {'thinglst': thinglst})
