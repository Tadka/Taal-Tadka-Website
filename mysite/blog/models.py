import datetime
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
