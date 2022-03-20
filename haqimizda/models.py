from django.db import models

# Create your models here.
class Ishtirokchilar(models.Model):
	name = models.CharField(max_length=255)
	about = models.TextField(blank=True)
	rasm = models.ImageField(upload_to='photos/%Y/%m/%d')


	def __str__(self):
		return self.name