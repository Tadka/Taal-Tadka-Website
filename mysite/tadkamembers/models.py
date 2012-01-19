from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='tadka_user')
	bio = models.CharField(max_length=2000, default=" ")
	year = models.CharField(max_length=20, default=" ")
	major = models.CharField(max_length=50, default=" ")
	vocalparts = models.CharField(max_length=100, default="")

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender = User)
