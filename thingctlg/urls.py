from django.urls import path
from . import views

app_name = 'thingctlg'
urlpatterns = [
    path('thinglst/', views.thinglist, name='thinglst'),
    path('uomlst/', views.uomlist, name='uomlst'),
]