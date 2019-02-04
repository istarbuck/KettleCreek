from django.db import models

# Create your models here.
class Menu(models.Model):
	category = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	description = models.TextField()
