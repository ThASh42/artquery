from django.urls import path
from . import views

app_name = 'querygenerator'

urlpatterns = [
    path('', views.index, name='index'),
]
