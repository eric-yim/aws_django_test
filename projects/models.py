from django.db import models

class Project(models.Model):
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.description


