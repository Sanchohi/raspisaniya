from django.contrib import admin
from .models import *
# Register your models here.

class RaspisAdmin(admin.ModelAdmin):
	list_display = ['title','raqam','xona','cat']


admin.site.register(Kunlar)
admin.site.register(Raspis,RaspisAdmin)