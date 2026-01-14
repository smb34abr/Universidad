from django.db import models

# Create your models here.
class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    curp = models.CharField(max_length=18)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    
    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5} {6} {7} {8}"
        return texto.format(self.id, self.nombre, self.apellido, self.curp, self.telefono, self.correo, self.fecha_nacimiento, self.genero, self.curp)
       