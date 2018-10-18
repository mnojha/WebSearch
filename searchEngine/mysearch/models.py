from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=200)
	description = models.CharField(max_length=1500)

class Signup(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=1500)
#	email = models.EmailField(max_length=200)
#	contact_no = models.IntegerField()

	