from __future__ import unicode_literals

from django.db import models

# Create your models here.
from PIL import Image
from django.contrib.auth.models import User	# Using DJango built-in Authentication model for now
# from shortuuidfield import ShortUUIDField


class Task(models.Model):
	user = models.OneToOneField(User, related_name='User', null=True)	
	task_name = models.CharField(max_length=20)
	task_desc = models.TextField(max_length=200)
	task_completed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='images/', default='images/none/no-img.png')
	doc = models.FileField(upload_to='doc/', default='doc/none/no-doc.pdf')

	def __str__(self):
		return '{0}'.format(self.task_name)
