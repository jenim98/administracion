from cProfile import label
from xml.dom.minidom import Attr
from django import forms
from isbh.models import *
from datetime import date
from django.forms.fields import DateField
from django.forms.widgets import Widget
from django.forms.widgets import NumberInput

'''
estandar de class: minuscula y si son dos palbras comenzar las siguientes con mayùscula
'''
# ----------TIPODOC----------
class tipoDocumentoSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.descripcion

class tipodocForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    descripcion= forms.CharField(
        label='Tipo de documento',
    )
    
# --------------------

# ----------ESTADO----------
class estadoForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    descripcion= forms.CharField(
        label='Estado',
    )
# --------------------

# ----------PAIS----------
class paisFormselector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre 

class paisForm (forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    nombre= forms.CharField(
        label='Nombre',
    )
# --------------------

# ----------PROVINCIA----------
class provinciaSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre

class provinciaForm (forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())    
    nombre= forms.CharField(
        label='Provincia',
    )
    pais= paisFormselector(
        label="País",
        queryset=Pais.objects.all().order_by('nombre'),
        to_field_name='id',
        empty_label='--Seleccione un País--'
    )
# --------------------

# ----------DEPARTAMENTO----------
class departamentoSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre

class departamentoForm (forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())    
    nombre= forms.CharField(
        label='Departamento',
    )
    pais= paisFormselector(
        label="País",
        queryset=Pais.objects.all().order_by('nombre'),

        to_field_name='id',
        empty_label='--Seleccione un País--',
        widget=forms.Select(attrs={"onchange":"cargarProvincia()"})
    )
    provincias= provinciaSelector(

        label="Provincia",
        queryset=Provincia.objects.all().order_by('nombre'),

        to_field_name='id',

        empty_label='--Seleccione una Provincia--',
        
        
    )
# --------------------

# ----------LOCALIDAD----------
class localidadForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    nombre= forms.CharField(
        label='Localidad',
    )
    pais= paisFormselector(
        label="País",
        queryset=Pais.objects.all().order_by('nombre'),

      to_field_name='id',

        empty_label='--Seleccione un País--',
        widget=forms.Select(attrs={"onchange":"cargarProvincia()"})
    )
    provincias= provinciaSelector(

        label="Provincia",
        queryset=Provincia.objects.all().order_by('nombre'),

        to_field_name='id',

        empty_label='--Seleccione un Provincia--',
        widget=forms.Select(attrs={"onchange":"cargarDepartamento()" , "disabled":"true"})
        
    )
    departamento= departamentoSelector(
        label="Departamento",
        queryset=Departamento.objects.all().order_by('nombre'),

        to_field_name='id',

        empty_label='--Seleccione un Departamento--',
        widget=forms.Select(attrs={"disabled":"true"})
    )
    
# --------------------

# ----------CARRERA----------
class carreraForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    nombre= forms.CharField(
        label='Carrera',
    )

class rangosedadesForm(forms.Form):
    descripcion= forms.CharField(
        label='Descripción',
    )
    desde= forms.IntegerField(
        label='Desde',
    )
    hasta= forms.IntegerField(
        label='Hasta',
    )
class coorteForm(forms.Form):
    descripcion= forms.CharField(
        label='Descripción',
    )
    ano_ini= forms.IntegerField(
        label='Año de inicio',
    )
    ano_fin= forms.IntegerField(
        label='Año de finalización',
    )

# --------------------

# ----------GENERO----------
class generoSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.descripcion
class generoForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    descripcion= forms.CharField(
        label='Género',
    )
# --------------------

# ----------COORTE----------
class coorteForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    now = date.today ()
    fechaInicio= forms.DateField(
        label='Fecha Apertura',
        widget=NumberInput(attrs={'type':'date'})
    )
    fechaFin=  forms.DateField(
        label='Fecha Cierre',
        widget=NumberInput(attrs={'type':'date'})
    )
class coorteSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.ano_ini
# --------------------

# ----------ALUMNOS----------
class alumnosForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    tipoDocumento= tipoDocumentoSelector(
        label="Tipo de documento",
        initial='0',
        queryset=Tipodoc.objects.all().order_by('descripcion'),
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
        queryset=Genero.objects.all().order_by('descripcion'),
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
    # coorte= coorteSelector(
    #     label="Coorte",
    #     queryset=Coorte.objects.all().order_by('id'),
    #     to_field_name='id',
    #     empty_label= '--Seleccione una Coorte--'
    # )
# --------------------

# ---------RANGOSEDADES----------
class rangosEdadesForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    now = date.today ()
    desde= forms.DateField(
        label='Desde',
        widget=NumberInput(attrs={'type':'date'})
    )
    hasta =  forms.DateField(
        label='Hasta',
        widget=NumberInput(attrs={'type':'date'})
    )
#-------------------
#-------TIPODECARRERA------
class tipodeCarreraForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    descripcion= forms.CharField(
        label='Tipo de carrera',
    )    
#-------------
#------MODALIDADDEDICTADO-------
class modalidaddeDictadoForm(forms.Form):
    id = forms.CharField(widget = forms.HiddenInput())
    descripcion= forms.CharField(
        label='Modalidad de dictado',
    )
   