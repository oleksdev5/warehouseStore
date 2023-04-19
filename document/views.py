from django.shortcuts import render
from .models import Receipt, Shipment

def receiptlist(request):
    receiptlst = Receipt.objects.all()
    return render(request, 'document/receiptlst.html', {'receiptlst': receiptlst})

def shipmentlist(request):
    shipmentlst = Shipment.objects.all()
    return render(request, 'document/shipmentlst.html', {'shipmentlst': shipmentlst})
