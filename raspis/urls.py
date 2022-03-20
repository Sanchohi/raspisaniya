from django.urls import path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	# path('reg/',reg,name='reg'),
	path('cat/<int:cat_id>/',cat,name='cat'),
	path('reg/',Reg.as_view(),name='reg')

]