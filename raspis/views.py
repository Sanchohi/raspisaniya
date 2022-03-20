from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import *
from googletrans import Translator
translator = Translator()
# Create your views here.

def home(request):
	if request.method == 'GET':
		f = request.GET.get('q','')
		print(f)
		e = translator.translate(f, dest='uz').text
		print(e)
	a = Kunlar.objects.all()
	return render(request,'index.html',{'a':a,'d':0,'e':e,'f':f})

def cat(request,cat_id):
	b = Raspis.objects.filter(cat_id=cat_id)
	a = Kunlar.objects.all()
	return render(request,'index.html',{'a':a,'b':b,'d':cat_id})

'''def reg(request):
	return render(request,'contact.html')'''

class Reg(CreateView):
	form_class = Newuser
	template_name = 'contact.html'
	success_url = reverse_lazy('login')