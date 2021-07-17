from django.db import models

# Create your models here.

class bModel(models.Model):
	name=models.CharField(max_length=30)
	phone=models.IntegerField()
	email=models.EmailField(max_length=100,primary_key=True)
	balance=models.FloatField(max_length=100)

	def __str__(self):
		return self.name

class tModel(models.Model):
	send=models.CharField(max_length=30)
	receive =models.CharField(max_length=30)
	amount=models.FloatField(max_length=100)
	transtype=models.CharField(max_length=30)
	dt = models.CharField(max_length=30)


	def __str__(self):
		return self.send
	
	