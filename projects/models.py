from django.db import models

class Project(models.Model):
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    url_str = models.CharField(max_length=255,default='erics-work')
    def __str__(self):
        return self.description


