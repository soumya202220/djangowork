from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='reg'),
    path('log/',views.log,name='log'),
    
]
