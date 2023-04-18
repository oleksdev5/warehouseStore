from django.urls import path
from . import views

app_name = 'things'
urlpatterns = [
    path('thinglst/', views.thinglist, name='thinglst'),
]