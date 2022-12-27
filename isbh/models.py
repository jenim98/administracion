from django.db import models

# Create your models here.
class Genero (models.Model):
    id= models.AutoField (
        primary_key= True
    )
    descripcion= models.TextField (
        max_length= 45, 
        null= False,
        blank= False
    )

class Tipodoc(models.Model):
    id=models.AutoField(
        primary_key=True
    )
    descripcion=models.TextField(
        max_length=45,
        null=False,
        blank=False)
    
class Pais(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    nombre= models.TextField(
        max_length= 45,
        null= False,
        blank= False
    )

class Provincia(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    nombre= models.TextField(
        max_length= 45,
        null= False,
        blank= False
     )
    pais_id= models.ForeignKey(
        Pais,
        null= False,
        blank= False,
        on_delete= models.PROTECT
     )

class Departamento(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    nombre= models.TextField(
        max_length= 45,
        null= False,
        blank= False
    )
    provincia_id= models.ForeignKey(
        Provincia,
        null= False,
        blank= False,
        on_delete= models.PROTECT
    ) 


class Localidad(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    nombre= models.TextField(
        max_length= 45,
        null= False,
        blank= False
    )
    departamento_id= models.ForeignKey(
        Departamento,
        null= False,
        blank= False,
        on_delete= models.PROTECT
    ) 

class Estado(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    descripcion= models.TextField(
        max_length= 45,
        null= False,
        blank= False
    )
    
class Coorte (models.Model):
    id= models.AutoField (
        primary_key= True
    )
    ano_ini= models.DateField(
        null= False,
        blank= False
    )
    ano_fin= models.DateField(
        null= False,
        blank= False
    )
class Carrera(models.Model):
    id=models.AutoField(
        primary_key=True
    )
    nombre=models.TextField(
        max_length=45,
        null=False,
        blank=False
    )
class Carreraxcoorte(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    carrera_id=models.ForeignKey(
        Carrera,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )    
   
    Coorte_id=models.ForeignKey(
        Coorte,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )    
class Rangosedades(models.Model):
    id=models.AutoField(
        primary_key=True
    )
    desde=models.DateField(
        max_length=3,
        null=False,
        blank=False)
  
    hasta=models.DateField(
        max_length=3,
        null=False,
        blank=False
    )

class Alumnos(models.Model):
    id=models.AutoField(
        primary_key=True,
        null=False,
        blank=False)
     

    Fechanac=models.DateField(
        null=False,
        blank=False)
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
    Apellido=models.TextField(
        max_length=40,
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
    LocalidadNac_id= models.ForeignKey(
        Localidad,
        related_name='LocalidadNac',
        null= False,
        blank= False,
        on_delete= models.PROTECT
    )
    LocalidadVive_id= models.ForeignKey(
        Localidad,
        related_name='LocalidadVive',
        null= False,
        blank= False,
        on_delete= models.PROTECT 
    )
    
class Tipodecarrera(models.Model):
    id=models.AutoField(
        primary_key=True
    )
    descripcion=models.TextField(
        max_length=45,
        null=False,
        blank=False
    )
    
class Modalidaddedictado(models.Model):
    id=models.AutoField(
        primary_key=True
    )
    descripcion=models.TextField(
        max_length=45,
        null=False,
        blank=False
    )
    
class AlumnosxCarreraxcoorte(models.Model):
    id= models.AutoField(
        primary_key= True
    )
    Carreraxcoorte_id=models.ForeignKey(
        Carreraxcoorte,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    
    Alumnos_id=models.ForeignKey(
        Alumnos,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )    
   
   
    Estado_id=models.ForeignKey(
        Estado,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )   
    
