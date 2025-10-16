from django.contrib import admin
from django.urls import path, include

app_name = 'notas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/', include(('notas.urls', 'notas'), namespace='notas'))
]
