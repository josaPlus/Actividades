from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notas')

    def __str__(self):
        return self.titulo
    
    def creado_recientemente(self):
        return self.fecha_de_creacion >= timezone.now() - datetime.timedelta(days=1)
    
    
