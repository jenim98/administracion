from django.db import models
from isbh.models import *

# Create your models here.
class Cursos (models.Model):
    id=models.AutoField(
        primary_key= True,
        null= False,
        blank= False
    )
    nombre=models.TextField(
        max_length=45,
        null= False,
        blank= False
    )

class MododeRendir (models.Model):
    id=models.AutoField(
    primary_key= True,
    null= False,
    blank= False
    )
    nombre= models.TextField(
        max_length=45,
        null= False,
        blank= False
    )
class EstadoMateriaAlumno (models.Model):
    id=models.AutoField(
        primary_key= True,
        null= False,
        blank= False
    )
    descripcion= models.TextField(
        max_length=45,
        null= False,
        blank= False
    )

class Profesores(models.Model):
    id=models.AutoField(
    primary_key=True,
    null=False,
    blank=False
)
    Fechanac=models.DateField(
        null=False,
        blank=False
)
    Documento=models.TextField(
    max_length=15,
    null=False,
    blank=False
)
    Apellido=models.TextField(
    max_length=40,
    null=False,
    blank=False
)
    Nombres=models.TextField(
    max_length=50,
    null=False,
    blank=False
)
    Direccion=models.TextField(
    max_length=50,
    null=False,
    blank=False
)
    Telefono=models.TextField(
    max_length=40,
    null=False,
    blank=False
)
    Email=models.TextField(
    max_length=45,
    null=False,
    blank=False
)
    Tipodoc_id= models.ForeignKey(
    Tipodoc,
    null= False,
    blank= False,
    on_delete= models.PROTECT
)
    Genero_id= models.ForeignKey(
    Genero,
    null= False,
    blank= False,
    on_delete= models.PROTECT
)
    LocalidadVive_id= models.ForeignKey(
    Localidad,    
    null= False,
    blank= False,
    on_delete= models.PROTECT 
)
    Nlegajo= models.TextField(
    max_length=40,    
    null = False,
    blank = False
)


class Materias(models.Model):
    id= models.AutoField(
    primary_key = True,
    null = False,
    blank=False
)    
    nombre= models.TextField(
    max_length =45,
    null=False,
    blank=False
)
    CargaHoraria= models.IntegerField(
    max_length=10,
    null=False,
    blank=False   
)
    Profesores_id=models.ForeignKey(
    Profesores,
    null=False,
    blank=False,
    on_delete= models.PROTECT
)
    Cursos_id=models.ForeignKey(
    Cursos,
    null=False,
    blank=False,
    on_delete= models.PROTECT
)
    MododeRendir_id=models.ForeignKey(
    MododeRendir,
    null=False,
    blank=False,
    on_delete= models.PROTECT
)
    
    Carrera_id=models.ForeignKey(
    Carrera,
    null=False,
    blank=False,
    on_delete= models.PROTECT
)

class Correlatividad (models.Model):
    id=models.AutoField (
    primary_key= True,
    null=False,
    blank=False
)
    habilitante=models.ForeignKey(
    Materias,    
    related_name='habilitante',
    null=False,
    blank=False,
    on_delete= models.PROTECT
)
    correlativa=models.ForeignKey(
    Materias,
    related_name='correlativa',
    null=False,
    blank=False,
    on_delete= models.PROTECT
)
