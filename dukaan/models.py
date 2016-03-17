from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# creating a model for Watch

class Watch(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=30)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2,max_digits=9)
    stock = models.IntegerField(default=0)


    def __unicode__(self):
        return "%s,  %d" %(self.company, self.stock)



