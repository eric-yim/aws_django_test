from django.db import models

class Project(models.Model):
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=32,default='ML')
    pub_date = models.DateTimeField('date published')
    url_str = models.CharField(max_length=255,default='erics-work')
    image_url = models.CharField(max_length=255,default='<i class="icon-screen-smartphone text-primary"></i>')
    body_html = models.TextField(default='')
    snippet = models.TextField(default='')
    def __str__(self):
        return self.description


