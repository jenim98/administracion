from django import forms
from isbh.models import *
from datetime import date
from django.forms.fields import DateField
from django.forms.widgets import Widget
from django.forms.widgets import NumberInput
from materias.models import *
# ----------PROFESORES----------

class generoSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.descripcion
class tipoDocumentoSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.descripcion


class profesoresForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    tipoDocumento= tipoDocumentoSelector(
        label="Tipo de documento",
        initial='0',
        queryset=Tipodoc.objects.all().order_by('id'),
        to_field_name='id'
        )
    documento= forms.CharField(
        label='Documento *'
    )
    nombre= forms.CharField(
        label='Nombre',
    )
    apellido= forms.CharField(
        label='Apellido',
    )
    genero = generoSelector(
        label="Género *",
        initial='0',
        queryset=Genero.objects.all().order_by('id'),
        to_field_name='id'
    )
    fechaNacimiento= forms.DateField(
        label='Fecha de nacimiento *',
        widget=NumberInput(attrs={'type':'date'})
    )
    telefono= forms.CharField(
        label='Telefono'
    )
    email= forms.EmailField(
        label='Email'
    )
    
    # ----------CURSOS----------
class cursoSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.descripcion
    
class cursoForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    descripcion= forms.CharField(
        label='Curso',
    )
        # ----------MATERIAS----------
class profesorSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '{}, {}'.format(obj.Apellido, obj.Nombres)

class cursosSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre
    
class mododerendirSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre
    
class carreraSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre
    
class materiaForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
     
    nombre= forms.CharField(
        label='Nombre',
    )
    CargaHoraria= forms.IntegerField(
        label='Carga horaria',
    )
    Profesores_id=profesorSelector(
        label="Profesor",
        initial='0',
        queryset=Profesores.objects.all().order_by('Apellido'),
        to_field_name='id'
    )
    Cursos_id=cursosSelector(
        label="Cursos",
        initial='0',
        queryset=Cursos.objects.all().order_by('nombre'),
        to_field_name='id'
    )
    MododeRendir_id=mododerendirSelector(
        label="Modo de rendir",
        initial='0',
        queryset=MododeRendir.objects.all().order_by('nombre'),
        to_field_name='id'
    )
    Carrera_id  = forms.CharField(widget = forms.HiddenInput())
   
    
class mododerendir(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    nombre=forms.CharField(
        label='Modo de rendir',
    )
