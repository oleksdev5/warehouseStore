from django.urls import path
from . import views

app_name = 'companyctlg'
urlpatterns = [
    path('companylst/', views.companylist, name='companylst'),
    path('agreementlst/', views.agreementlist, name='agreementlst'),
    path('ourfirmlst/', views.ourfirmlist, name='ourfirmlst'),
]