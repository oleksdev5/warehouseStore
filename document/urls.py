from django.urls import path
from . import views

app_name = 'document'
urlpatterns = [
    path('receiptlst/', views.receiptlist, name='receiptlst'),
    path('shipmentlst/', views.shipmentlist, name='shipmentlst'),
]