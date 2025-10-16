from django.contrib import admin
from .models import Nota

# Register your models here.
class NotaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_de_creacion', 'creado_recientemente']
    search_fields = ['titulo']
    list_filter = ['fecha_de_creacion']
    fields = ['titulo', 'contenido']


admin.site.register(Nota, NotaAdmin)