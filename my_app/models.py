from django.db import models

# Create your models here.
#Django ORM - Object Relational Mapper - Banco de dados
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()