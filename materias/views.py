from django.shortcuts import render, redirect
from django.shortcuts import render

from datetime import datetime,date
from materias.forms import *
from materias.models  import *
from django.db.models import ProtectedError
from django.contrib import messages

# Create your views here.
# ----------CURSOS----------
def cursosCrearFormulario (request, id):
    formulario= cursoForm()
    if id != 0:
        cursos1=Cursos.objects.get(pk=id)
        formulario.fields['id'].initial=cursos1.id
        formulario.fields['descripcion'].initial=cursos1.nombre
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarcursos.html',{'form':formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso pais ---
def guardarCursos(request):
    if request.method=='POST':
        if int(request.POST['id'])>0: 
            xid=request.POST['id']
            registro=Cursos.objects.get(pk=xid)
            registro.nombre=request.POST['descripcion']   
               
        else:
            registro=Cursos()
            registro.nombre=request.POST['descripcion'] 
        registro.save()
    return redirect ('cursos')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario un pais en especifico ---
def consultarCurso (request):
    cursos1 = Cursos.objects.all().order_by('id')
    return render (request, "cursos.html",{"cursos":cursos1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
def cursosEliminar (request, id):
    try: 
        eliminarCursos1 = Cursos.objects.get(pk=id)
        eliminarCursos1.delete()
        return redirect ('cursos')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarCursos1.descripcion+ ',tiene registros anexados')
        return redirect ('cursos')   
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---    
# --------------------
# Create your views here.
# ----------MATERIAS----------
def materiasCrearFormulario (request, id, idcarrera):
    carrera1=Carrera.objects.get(pk=idcarrera)
    formulario= materiaForm()
    formulario.fields['Carrera_id'].initial=carrera1.id 
    if id != 0:
        materias1=Materias.objects.get(pk=id)
        formulario.fields['id'].initial=materias1.id
        formulario.fields['nombre'].initial=materias1.nombre
        formulario.fields['CargaHoraria'].initial=materias1.CargaHoraria
        formulario.fields['Profesores_id'].initial=materias1.Profesores_id.id
        formulario.fields['Cursos_id'].initial=materias1.Cursos_id.id
        formulario.fields['MododeRendir_id'].initial=materias1.MododeRendir_id.id
        
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarmaterias.html',{'form':formulario, 'carrera':carrera1})

def guardarMaterias(request):
    if request.method=='POST':
        xid=request.POST['id']
        if int(request.POST['id'])>0:    
            registro=Materias.objects.get(pk=xid)   
        else:
            registro=Materias()
    registro.nombre=request.POST['nombre']
    registro.CargaHoraria=request.POST['CargaHoraria']
    profesores=Profesores.objects.get(pk=request.POST['Profesores_id'])
    cursos=Cursos.objects.get(pk=request.POST['Cursos_id'])
    modoDeRendir=MododeRendir.objects.get(pk=request.POST['MododeRendir_id'])
    carrera=Carrera.objects.get(pk=request.POST['Carrera_id'])
    registro.Profesores_id=profesores
    registro.Cursos_id=cursos
    registro.MododeRendir_id=modoDeRendir
    registro.Carrera_id=carrera
    registro.save()
    materias=Materias.objects.filter(Carrera_id=carrera).order_by('nombre')
    return render(request,'materias.html',{"materias":materias,"carrera":carrera})

def consultarMaterias (request, id):
    carrera1=Carrera.objects.get(pk = id)
    materias1=Materias.objects.filter(Carrera_id=carrera1).order_by('nombre')
    return render (request, "materias.html",{"materias":materias1,"carrera":carrera1})

def materiasEliminar (request, id, idcarrera):
    carrera1=Carrera.objects.get(pk=idcarrera)
    materias1=Materias.objects.filter(Carrera_id=carrera1).order_by('nombre')
    try: 
        eliminarMaterias1 = Materias.objects.get(pk=id)
        eliminarMaterias1.delete()
        return render (request,'materias.html',{"materias":materias1,"carrera":carrera1})
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarMaterias1.nombre+ ',tiene registros anexados')
        return render (request,'materias.html',{"materias":materias1,"carrera":carrera1})   
    
 
# --------------------

# ----------PROFESORES----------
def profesoresCrearFormulario (request, id):
    formulario= profesoresForm()
    if id != 0:
        registro = Profesores.objects.get(pk=id)
        formulario.fields['id'].initial = registro.id
        formulario.fields['tipoDocumento'].initial = registro.Tipodoc_id.id
        formulario.fields['nombre'].initial = registro.Nombres
        formulario.fields['apellido'].initial = registro.Apellido
        formulario.fields['documento'].initial = registro.Documento
        formulario.fields['genero'].initial = registro.Genero_id.id
        ano=registro.Fechanac.year
        mes=registro.Fechanac.month
        dia=registro.Fechanac.day
        formatoFecha = str(dia) + '-' + str(mes) + '-' + str(ano)
        formatoFecha=datetime.strptime(formatoFecha,'%d-%m-%Y').date()
        formulario.fields['fechaNacimiento'].initial = formatoFecha
        formulario.fields['telefono'].initial = registro.Telefono
        formulario.fields['email'].initial = registro.Email
        localidadResidencia = registro.LocalidadVive_id.id
        localidadResidenciaNombre = registro.LocalidadVive_id.nombre
        direccion = registro.Direccion
        tipo = 1
        
    else:
        formulario.fields['id'].initial = 0
        tipo = 0
        localidadResidencia = ""
        localidadResidenciaNombre = ""
        direccion = ""
    return render (request, 'agregarprofesores.html', {'form':formulario,
                                                    'localidadResidencia':localidadResidencia,
                                                    'localidadResidenciaNombre':localidadResidenciaNombre,
                                                    'direccion':direccion,
                                                    'tipo':tipo})

def guardarProfesores(request):
    if request.method=='POST':
        Nombre1=request.POST['nombre']
        Apellido1=request.POST['apellido']
        TipoDocumento1=request.POST['tipoDocumento']
        Tipodoc1=Tipodoc.objects.get(pk=TipoDocumento1)
        Documento1=request.POST['documento']
        Genero1=request.POST['genero']
        Gen1=Genero.objects.get(pk=Genero1)
        FechaNacimiento1=request.POST['fechaNacimiento']
        Telefono1=request.POST['telefono']
        Email1=request.POST['email']
        LocalidadResidencia1=request.POST['id_localidadRes']
        LocalResid1=Localidad.objects.get(pk=LocalidadResidencia1)
        Direccion1=request.POST['direccion']

        if int(request.POST['id'])>0:
            xid=request.POST['id']
            Profesor1=Profesores.objects.get(pk=xid)
            Profesor1.Nombres=Nombre1
            Profesor1.Apellido=Apellido1
            Profesor1.Tipodoc_id=Tipodoc1
            Profesor1.Documento=Documento1
            Profesor1.Genero_id=Gen1
            Profesor1.Fechanac=FechaNacimiento1
            Profesor1.Telefono=Telefono1
            Profesor1.Email=Email1
            Profesor1.LocalidadVive_id=LocalResid1
            Profesor1.Direccion=Direccion1
            Profesor1.save()
            
        else:
            Profesor1=Profesores(
                Nombres=Nombre1,
                Apellido=Apellido1,
                Tipodoc_id=Tipodoc1,
                Documento=Documento1,
                Genero_id=Gen1,
                Fechanac=FechaNacimiento1,
                Telefono=Telefono1,
                Email=Email1,
                LocalidadVive_id=LocalResid1,
                Direccion=Direccion1,
            )
            Profesor1.save()
    return redirect ('profesor')

def consultarProfesores(request):
    Profesores1=Profesores.objects.all().order_by('Apellido')
    return render (request,"profesores.html",{"profesor":Profesores1})

def traerLocalidad(request):
    Localidad1=Localidad.objects.all().order_by('departamento_id__provincia_id')
    return render (request, "traerLocalidad.html",{"localidades":Localidad1})

def profesoresEliminar (request, id):
    try: 
        eliminarProfesor1 = Profesores.objects.get(pk=id)
        eliminarProfesor1.delete()
        return redirect ('profesor')
    except ProtectedError as e:
        eliminarProfesor1 = Profesores.objects.get(pk=id)
        messages.info(request, 'Error al eliminar '+eliminarProfesor1.Nombres+', '+eliminarProfesor1.Apellido+ ', tiene registros anexados')
        return redirect ('profesor') 
    
    #--------MODODERENDIR-------
def consultarMododerendir(request):
    Modo1 = MododeRendir.objects.all().order_by('nombre')
    return render (request,"mododerendir.html",{'mododerendir':Modo1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
   
def mododerendirCrearFormulario (request, id):
    Formulario= mododerendir()
    if id !=0:
        Modo1=MododeRendir.objects.get(pk=id)
        Formulario.fields['id'].initial = Modo1.id
        Formulario.fields['nombre'].initial=Modo1.nombre
    else:
        Formulario.fields['id'].initial=0
    return render (request, 'agregarmododerendir.html', {'form':Formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso carrera ---

def guardarMododerendir(request):
    if request.method=='POST':
        xid=request.POST['id']
        descripcion=request.POST['nombre']
        if int(request.POST['id'])>0:
            registro=MododeRendir.objects.get(pk=xid)
        else:
            registro=MododeRendir()
    registro.nombre=descripcion      
    registro.save()
    return redirect ('mododerendir')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario una carrera en especifico ---

def mododerendirEliminar (request, id):
    try: 

        eliminarmodo1 = MododeRendir.objects.get(pk=id)
        eliminarmodo1.delete()
        return redirect ('mododerendir')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarmodo1.nombre+ ',tiene registros anexados')
        return redirect ('mododerendir') 
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---
    