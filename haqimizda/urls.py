from .views import *
from django.urls import path

urlpatterns=[
	path('haqimizda/',haq,name='haq'),
	path('oqi/<int:oqi_id>/',oqi,name='oqi'),
]