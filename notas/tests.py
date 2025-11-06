from django.test import TestCase
from .models import Nota
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# Create your tests here.
class NotaModelTest(TestCase):
    def setUp(self):
        """
        Set up para los tests creando un usuario de prueba.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_crear_nota(self):
        """
        Verifica que una nota se cree correctamente con todos los campos asignados.
        """
        nota = Nota.objects.create(
            usuario=self.user,
            titulo='Test Nota',
            contenido='Contenido de prueba',
            fecha_de_creacion=timezone.now()
        )
        nota.save()

        self.assertEqual(nota.usuario, self.user)
        self.assertEqual(nota.titulo, nota.titulo)
        self.assertEqual(nota.contenido, nota.contenido)
        self.assertIsNotNone(nota.fecha_de_creacion)
    
    def test_str_nota(self):
        """
        Verifica que el método __str__ del modelo Nota retorne el título.
        """
        nota = Nota.objects.create(
            usuario=self.user,
            titulo='Título de prueba',
            contenido='Contenido de ejemplo',
            fecha_de_creacion=timezone.now()
        )
        nota.save()

        self.assertEqual(str(nota), nota.titulo)

class NotaViewsTest(TestCase):
    def setUp(self):
        # Crear usuario y nota de prueba
        self.user = User.objects.create_user(username='usuario', password='12345')
        self.nota = Nota.objects.create(
            usuario=self.user,
            titulo='Nota del usuario',
            contenido='Contenido visible solo para el usuario autenticado'
        )
    
    def test_lista_notas_requiere_autenticacion(self):
        """
        Verifica que un usuario no autenticado sea redirigido al login.
        """
        url = reverse('notas:lista_notas')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_lista_notas_usuario_autenticado(self):
        """
        Verifica que un usuario autenticado pueda ver su lista de notas.
        """
        self.client.force_login(self.user)

        url = reverse('notas:lista_notas')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nota del usuario')
