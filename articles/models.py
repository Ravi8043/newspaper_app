from django.db import models

# Create your models here.
class ArticlesModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True,blank=True)
    created_by = models.CharField(max_length=255, null=True, blank= True)