from django.db import models

# Create your models here.
class Img(models.Model):
	name = models.CharField(max_length=20)
	img_file = models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.name