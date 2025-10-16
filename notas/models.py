from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def creado_recientemente(self):
        return self.fecha_de_creacion >= timezone.now() - datetime.timedelta(days=1)
    
    
