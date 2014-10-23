from django.db import models

class UrlTable(models.Model):
    original_url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=50)
   
    def __unicode__(self):
        return self.original_url
