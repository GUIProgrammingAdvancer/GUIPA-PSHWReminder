from django.db import models

# Create your models here.

class Homework(models.Model):
	date = models.CharField(max_length=100)
	homework = models.CharField(max_length=1000)
	preview = models.CharField(max_length=1000)
	topic = models.CharField(max_length=1000)
	guide = models.CharField(max_length=1000)
	target = models.CharField(max_length=1000)
	opentopic = models.CharField(max_length=1000)
	def __str__(self):
		return self.date
