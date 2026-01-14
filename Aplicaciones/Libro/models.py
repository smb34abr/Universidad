from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_publicacion = models.DateField()
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    editorial = models.CharField(max_length=100)
    stock = models.IntegerField()
    
    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5} {6} {7} {8}"
        return texto.format(self.id, self.titulo, self.isbn, self.precio, self.fecha_publicacion, self.autor, self.genero, self.editorial, self.stock)