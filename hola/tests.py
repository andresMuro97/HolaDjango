from django.test import TestCase
from hola.models import Articulo 
from django.db import IntegrityError

class TestSmoke(TestCase):
    def test_smoke_test(self):
        self.assertEqual(2 + 2, 4)

class BaseModelTest(TestCase):

    def test_agrega_articulo(self):
                articulo = Articulo.objects.create(
                    nombre = 'Xbox',
                    precio = 321.30,
                    descripcion = 'Consola de juegos'
                )
                articulo_uno = Articulo.objects.first()

                self.assertEqual(articulo, articulo_uno)
                self.assertEqual(str(articulo_uno), 'Xbox')
        
    def test_articulo_nombre_null(self):
            with self.assertRaises(IntegrityError):
                articulo = Articulo.objects.create(
                    nombre = None,
                    precio = 321.30,
                    descripcion = 'Consola de juegos'
                )
                base.full_clean()   
    
    def test_articulo_precio_null(self):
            with self.assertRaises(IntegrityError):
                articulo = Articulo.objects.create(
                    nombre = "Xbox",
                    precio = None,
                    descripcion = 'Consola de juegos'
                )
                base.full_clean()  