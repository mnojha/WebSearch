from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=200)
	description = models.CharField(max_length=1500)

#class Signup(AbstractBaseUser):
#	username = models.CharField(max_length=50)
#	email = models.EmailField(max_length=50, blank=True, null=True, default='')
#	password = models.CharField(max_length=1500)
#	objects = UserManager()

#	def __str__(self):
#		return self.username

#class SignupForm(ModelForm):
#	class Meta:
#		model = Signup
#		fields = '_all_'

#	email = models.EmailField(max_length=200)
#	contact_no = models.IntegerField()

	