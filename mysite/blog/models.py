import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    bio = models.CharField(max_length=2000)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender = User)
