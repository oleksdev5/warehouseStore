from django.shortcuts import render
from .models import Company, Agreement, Ourfirm

def companylist(request):
    companylst = Company.objects.all()
    return render(request, 'companyctlg/companylst.html', {'companylst': companylst})


def agreementlist(request):
    agreementlst = Agreement.objects.all()
    return render(request, 'companyctlg/agreementlst.html', {'agreementlst': agreementlst})


def ourfirmlist(request):
    ourfirmlst = Ourfirm.objects.all()
    return render(request, 'companyctlg/ourfirmlst.html', {'ourfirmlst': ourfirmlst})