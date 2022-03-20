from django.db import models

# Create your models here.

class Kunlar(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Raspis(models.Model):
	raqam = models.PositiveSmallIntegerField(default=0)
	title = models.CharField(max_length=255)
	xona = models.CharField(max_length=9)
	cat = models.ForeignKey(Kunlar,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['raqam']

