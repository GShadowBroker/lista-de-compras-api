from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    data = models.DateTimeField(auto_now=True)

    ITEM_CHOICES = [
        ('0', 'normal'),
        ('+1', 'alto'),
        ('-1', 'baixo'),
    ]

    prioridade = models.CharField(max_length=2, choices=ITEM_CHOICES, default='0')

    class Meta:
        ordering = ['data'] ###### Mudar para ordem de data E prioridade!*

    def __str__(self):
        return self.nome