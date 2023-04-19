from django.urls import path, include
from . import views

app_name = 'mainscreen'
urlpatterns = [
    path('', views.index, name='index'),
    path('thngctlg/', include('thingctlg.urls', namespace='thingctlg')),
    path('cmpnctlg/', include('companyctlg.urls', namespace='companyctlg')),
    path('dcmnt/', include('document.urls', namespace='document')),
]