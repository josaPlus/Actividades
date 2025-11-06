from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


app_name = 'notas'

urlpatterns = [
    path('', RedirectView.as_view(url='notas/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('notas/', include(('notas.urls', 'notas'), namespace='notas')),
    path('encuestas/', RedirectView.as_view(url='/notas/', permanent=True))
]
