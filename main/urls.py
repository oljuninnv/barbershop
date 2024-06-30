from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('record', views.records,name='record'),
    path('record/thanks', views.thanks,name='thanks'),
]