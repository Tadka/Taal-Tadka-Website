from django.db import models

# Create your models here.

class Song(models.Model):
	song = models.CharField(max_length=200)
	arrangedby = models.CharField(max_length=200)
	importance = models.IntegerField()
	soundcloudpreview = models.CharField(max_length=200, default='NULL')
	ituneslink = models.CharField(max_length=200, default='NULL')
	def __unicode__(self):
		return self.song
