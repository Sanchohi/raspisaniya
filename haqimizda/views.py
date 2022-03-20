from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def haq(request):
	a = Ishtirokchilar.objects.all()
	return render(request,'haqimizda.html',{'a':a})

def oqi(request,oqi_id):
	a = get_object_or_404(Ishtirokchilar,pk=oqi_id)
	return render(request,'oqi.html',{'a':a})


