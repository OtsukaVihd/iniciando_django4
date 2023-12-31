from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name


# Create your models here.
#Django ORM - Object Relational Mapper - Banco de dados
class Post(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Título')
    # null para BD
    # blank para o formulário
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Corpo do Artigo')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Artigo'
        #verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title
