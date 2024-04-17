from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('nome',) #Retornando na ordem alfabética
        verbose_name_plural = 'Categorias' #Colocando no plural a tabela Categoria
        
    def __str__(self):
        return self.nome   #Retornando os nomes nas categorias
    
class Item(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='items', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome