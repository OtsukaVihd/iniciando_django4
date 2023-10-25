from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Django ORM - Object Relational Mapper - Banco de dados
class Post(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Título')
    # null para BD
    # blank para o formulário
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Corpo do Artigo')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')


    class Meta:
        verbose_name = 'Artigo'
        #verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title
