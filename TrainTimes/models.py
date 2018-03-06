from django.db import models

# Create your models here.

class train(models.Model):
	train_name = models.CharField(max_length=10)
	stop_name = models.CharField(max_length=100)
	direction = models.CharField(max_length=10)
	stop_key = models.CharField(max_length=100, default='0')
	stop_id = models.CharField(max_length=10, default='0')
	parent_id = models.CharField(max_length=20, default='0')
	#time1 = models.CharField(max_length=3)
	#time2 = models.CharField(max_length=3)
	
	#def __str__(self):
		#return self.train_name + ' - ' + self.stop_name

class stops(models.Model):
	stop_name = models.CharField(max_length=30)
	stop_id = models.CharField(max_length=10)
	