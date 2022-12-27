
import string
from django.shortcuts import render, redirect
from django.http import JsonResponse,FileResponse
from isbh.forms import *
from isbh.models import *
from django.db.models import ProtectedError
from django.contrib import messages
from django.db.models import Count
from datetime import date
from django.forms.fields import DateField
from datetime import datetime
from isbh.fechas import *
from datetime import timedelta 
from dateutil.relativedelta import relativedelta 


# Create your views here.



'''
estandar funcion: minuscula y las siguientes en mayuscula
estandar de objeto(variable): mayuscula y las siguientes palabras en mayuscula
objeto=clase

para darle nombre a las URL de los html usaremos guardar + nombretabla / nuevo + nombretabla / consultar + nombretabla
en Consultar va el plural del nombretabla igual al for del html - Ejemplo {% for tabla in tablas%}

'''

# ----------PRINCIPAL----------
def principal (request):
    return render (request, 'inicio.html')
def principal2 (request):
    return render (request, 'otro.html')
def correlatividad (request):
    return render (request, 'correlatividad.html')
# --------------------

# ----------PAIS----------
def paisCrearFormulario (request, id):
    formulario= paisForm()
    if id != 0:
        pais1=Pais.objects.get(pk=id)
        formulario.fields['id'].initial=pais1.id
        formulario.fields['nombre'].initial=pais1.nombre
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarpais.html',{'form':formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso pais ---
def guardarPais(request):
    if request.method=='POST':
        if int(request.POST['id'])>0:
            xid=request.POST['id']
            registro=Pais.objects.get(pk=xid)   
        else:
            registro=Pais()
        registro.nombre=request.POST['nombre']
        registro.save()
    return redirect('pais')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario un pais en especifico ---
def consultarPais (request):
    pais1 = Pais.objects.all().order_by('id')
    return render (request, "pais.html",{"pais":pais1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
def paisEliminar (request, id):
    try: 
        eliminarPais1 = Pais.objects.get(pk=id)
        eliminarPais1.delete()
        return redirect ('pais')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarPais1.nombre+ ',tiene registros anexados')
        return redirect ('pais')   
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---    
# --------------------

# ----------TIPODOC----------
def tipodocCrearFormulario (request, id):
    formulario= tipodocForm()
    if id != 0:
        tipodoc1=Tipodoc.objects.get(pk=id)
        formulario.fields['id'].initial=tipodoc1.id
        formulario.fields['descripcion'].initial=tipodoc1.descripcion
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregartipodoc.html', {'form':formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso tipoDoc ---
def guardarTipodoc(request):
   if request.method=='POST':
        xid=request.POST['id']
        nombre=request.POST['descripcion']
        if int(request.POST['id'])>0:
            registro=Tipodoc.objects.get(pk=xid)
        else:
            registro=Tipodoc()
        registro.descripcion=request.POST['descripcion']  
        registro.descripcion=nombre    
        registro.save()
        return redirect ('tipo')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario un tipoDoc en especifico ---
def consultarTipodoc(request):
    Tipodoc1=Tipodoc.objects.all().order_by('id')
    return render (request, "tipodoc.html",{"tipodoc":Tipodoc1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
   
def tipodocEliminar (request, id):
    try: 
        eliminarTipodoc1 = Tipodoc.objects.get(pk=id)
        eliminarTipodoc1.delete()
        return redirect ('tipo')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarTipodoc1.descripcion+ ',tiene registros anexados')
        return redirect ('tipo')  
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---  
# --------------------

# ----------LOCALIDAD----------
def localidadCrearFormulario (request, id):
    Formulario= localidadForm()
    if id != 0:
        tipo = 1
        registro=Localidad.objects.get(pk=id)
        Formulario.fields['id'].initial=registro.id
        Formulario.fields['nombre'].initial=registro.nombre
        Formulario.fields['departamento'].initial=registro.departamento_id
        Formulario.fields['provincias'].initial=registro.departamento_id.provincia_id
        Formulario.fields['pais'].initial=registro.departamento_id.provincia_id.pais_id
    else:
        tipo=0
        Formulario.fields['id'].initial=0
    return render (request, 'agregarlocalidad.html', {'form':Formulario,'tipo':tipo})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso localidad ---
def localidadGuardar(request):
    if request.method=='POST':
        xid=request.POST['id']
        nombre=request.POST['nombre']
        departamento_id=request.POST['departamento']
        registroDepartamento=Departamento.objects.get(pk=departamento_id)
        if int(xid)>0:
            registro=Localidad.objects.get(pk=xid)
        else:
            registro=Localidad()
    registro.nombre=nombre 
    registro.departamento_id=registroDepartamento
    registro.save()
    return redirect ('localidad')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario una localidad en especifico ---
def consultarLocalidad (request):
    localidad1 = Localidad.objects.all().order_by('nombre')
    return render (request, "localidad.html",{"localidades":localidad1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
def localidadEliminar (request, id):
    try: 
        eliminarLocalidad1 = Localidad.objects.get(pk=id)
        eliminarLocalidad1.delete()
        return redirect ('localidad')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarLocalidad1.nombre+ ',tiene registros anexados')
        return redirect ('localidad')  
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---
# --------------------

# ----------CARRERA----------

def consultarCarrera (request):
    Carrera1 = Carrera.objects.all().order_by('nombre')
    return render (request,"carrera.html",{'carreras':Carrera1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
   
def carreraCrearFormulario (request, id):
    formulario= carreraForm()
    if id !=0:
        carrera1=Carrera.objects.get(pk=id)
        formulario.fields['id'].initial = carrera1.id
        formulario.fields['nombre'].initial=carrera1.nombre
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarcarrera.html', {'form':formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso carrera ---

def guardarCarrera(request):
    if request.method=='POST':
        xid=request.POST['id']
        nombre=request.POST['nombre']
        if int(request.POST['id'])>0:
            registro=Carrera.objects.get(pk=xid)
        else:
            registro=Carrera()
    registro.nombre=nombre        
    registro.nombre=request.POST['nombre']      
    registro.save()
    return redirect ('carrera')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario una carrera en especifico ---

def carreraEliminar (request, id):
    try: 
        eliminarCarrera1 = Carrera.objects.get(pk=id)
        eliminarCarrera1.delete()
        return redirect ('carrera')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarCarrera1.nombre+ ',tiene registros anexados')
        return redirect ('carrera') 
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---
    
# --------------------

# ----------PROVINCIA----------
def consultarProvincia (request):
    Provincia1 = Provincia.objects.all().order_by('id')
    return render (request, "provincia.html",{'provincias':Provincia1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---

def provinciaCrearformulario (request, id):
    formulario= provinciaForm()
    if id != 0:
        provincia1=Provincia.objects.get(pk=id)
        formulario.fields['id'].initial=provincia1.id
        formulario.fields['nombre'].initial=provincia1.nombre
        formulario.fields['pais'].initial=provincia1.pais_id
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarprovincia.html', {'form':formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso provincia ---
def provinciaGuardar(request):
    if request.method=='POST':
        xid=request.POST['id']
        nombre=request.POST['nombre']
        pais_id=request.POST['pais']
        registroPais=Pais.objects.get(pk=pais_id)
        if int(request.POST['id'])>0:
            registro=Provincia.objects.get(pk=xid)
        else:
            registro=Provincia()
    registro.nombre=nombre
    registro.pais_id=registroPais
    registro.save()
    return redirect ('provincia')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario una provincia en especifico ---
def cargarProvincia(request):
    if request.method == 'GET':
        registroPais=request.GET['id']
        provincias=Provincia.objects.filter(pais_id=registroPais)
        return JsonResponse(list(provincias.values('id','nombre')),safe=False)

def provinciaEliminar (request, id):
    try: 

        eliminarProvincias1 = Provincia.objects.get(pk=id)
        eliminarProvincias1.delete()
        return redirect ('provincia')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarProvincias1.nombre+ ',tiene registros anexados')
        return redirect ('provincia')   
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---

# --------------------

# ----------DEPARTAMENTO----------
def consultarDepartamento(request):
    Departamentos=Departamento.objects.all().order_by('nombre')
    return render (request,"departamento.html",{"departamentos":Departamentos})

def departamentoCrearFormulario (request, id):
    formulario=departamentoForm()
    if id != 0:
        tipo = 1
        departamento1=Departamento.objects.get(pk=id)
        formulario.fields['id'].initial=departamento1.id
        formulario.fields['nombre'].initial=departamento1.nombre
        formulario.fields['pais'].initial=departamento1.provincia_id.pais_id
        formulario.fields['provincias'].initial=departamento1.provincia_id
    else:
        tipo=0
        formulario.fields['id'].initial=0
    return render (request, 'agregardepartamento.html', {'form':formulario,'tipo':tipo})

def guardarDepartamento(request):
    if request.method=='POST':
        xid=request.POST['id']
        nombre=request.POST['nombre']
        provincia_id=request.POST['provincias']
        registroProvincia=Provincia.objects.get(pk=provincia_id)
        if int(request.POST['id'])>0:
            registro=Departamento.objects.get(pk=xid)
        else:
            registro=Departamento()
    registro.nombre=nombre
    registro.provincia_id=registroProvincia
    registro.save()
    return redirect ( 'departamento')

def cargarDepartamento(request):
    if request.method=='GET':
        Provincia1=request.GET['id']
        Departamento1=Departamento.objects.filter(provincia_id=Provincia1)
        return JsonResponse(list(Departamento1.values('id','nombre')),safe=False)

def departamentoEliminar (request, id):
    try: 

        eliminarDepartamento1 = Departamento.objects.get(pk=id)
        eliminarDepartamento1.delete()
        return redirect ('departamento')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarDepartamento1.nombre+ ',tiene registros anexados')
        return redirect ('departamento')   
# --------------------

# ----------ALUMNOS----------
def alumnosCrearFormulario (request, id):
    formulario= alumnosForm()
    if id != 0:
        registro = Alumnos.objects.get(pk=id)
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
        localidadNacimiento = registro.LocalidadNac_id.id
        localidadNacimientoNombre = registro.LocalidadNac_id.nombre
        localidadResidencia = registro.LocalidadVive_id.id
        localidadResidenciaNombre = registro.LocalidadVive_id.nombre
        direccion = registro.Direccion
        tipo = 1
        
    else:
        formulario.fields['id'].initial = 0
        tipo = 0
        localidadNacimiento = ""
        localidadNacimientoNombre = ""
        localidadResidencia = ""
        localidadResidenciaNombre = ""
        direccion = ""
    return render (request, 'agregaralumnos.html', {'form':formulario,
                                                    'localidadNacimiento':localidadNacimiento,
                                                    'localidadNacimientoNombre':localidadNacimientoNombre,
                                                    'localidadResidencia':localidadResidencia,
                                                    'localidadResidenciaNombre':localidadResidenciaNombre,
                                                    'direccion':direccion,
                                                    'tipo':tipo})

def guardarAlumnos(request):
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
        LocalidadNacimiento1=request.POST['id_localidadNac']
        LocalNacim1=Localidad.objects.get(pk=LocalidadNacimiento1)
        LocalidadResidencia1=request.POST['id_localidadRes']
        LocalResid1=Localidad.objects.get(pk=LocalidadResidencia1)
        Direccion1=request.POST['direccion']

        if int(request.POST['id'])>0:
            xid=request.POST['id']
            Alumno1=Alumnos.objects.get(pk=xid)
            Alumno1.Nombres=Nombre1
            Alumno1.Apellido=Apellido1
            Alumno1.Tipodoc_id=Tipodoc1
            Alumno1.Documento=Documento1
            Alumno1.Genero_id=Gen1
            Alumno1.Fechanac=FechaNacimiento1
            Alumno1.Telefono=Telefono1
            Alumno1.Email=Email1
            Alumno1.LocalidadNac_id=LocalNacim1
            Alumno1.LocalidadVive_id=LocalResid1
            Alumno1.Direccion=Direccion1
            Alumno1.save()
            
        else:
            Alumnos1=Alumnos(
                Nombres=Nombre1,
                Apellido=Apellido1,
                Tipodoc_id=Tipodoc1,
                Documento=Documento1,
                Genero_id=Gen1,
                Fechanac=FechaNacimiento1,
                Telefono=Telefono1,
                Email=Email1,
                LocalidadNac_id=LocalNacim1,
                LocalidadVive_id=LocalResid1,
                Direccion=Direccion1,
            )
            Alumnos1.save()
            cantidad = int(request.POST['cantidad'])
            estado1 = Estado.objects.get(pk=1)
            for i in range(cantidad):
                idCoorte = request.POST['registro'+str(i)]
                objetoIdCoorte = Carreraxcoorte.objects.get(pk=idCoorte)
                alumnosPorCoorte = AlumnosxCarreraxcoorte(
                    Carreraxcoorte_id = objetoIdCoorte,
                    Alumnos_id = Alumnos1,
                    Estado_id = estado1
                )
                alumnosPorCoorte.save()

    return redirect ('alumno')

def consultarAlumnos (request):
    Alumnos1=Alumnos.objects.all().order_by('Apellido')
    return render (request,"alumnos.html",{"alumnos":Alumnos1})

def traerLocalidad(request):
    Localidad1=Localidad.objects.all().order_by('departamento_id__provincia_id')
    return render (request, "traerLocalidad.html",{"localidades":Localidad1})

def alumnosEliminar (request, id):
    try: 
        eliminarAlumno1 = Alumnos.objects.get(pk=id)
        eliminarAlumno1.delete()
        return redirect ('alumno')
    except ProtectedError as e:
        eliminarAlumno1 = Alumnos.objects.get(pk=id)
        messages.info(request, 'Error al eliminar '+eliminarAlumno1.Nombres+', '+eliminarAlumno1.Apellido+ ', tiene registros anexados')
        return redirect ('alumno') 
    
def traerFecha(request):
    fechas = Coorte.objects.all().order_by('-ano_ini')
    return JsonResponse(list(fechas.values('id', 'ano_ini')),safe=False)

def cargarCarreraxCoorte(request):
    if request.method == 'GET':
        fechaCoorte = request.GET['id']
        coorte = Coorte.objects.get(pk=fechaCoorte)
        carrera = Carreraxcoorte.objects.filter(Coorte_id=coorte)
        return JsonResponse(list(carrera.values('id', 'carrera_id__nombre')),safe=False)

def eliminarAlumnoCoorte (request, id):
    eliminarAlumno = AlumnosxCarreraxcoorte.objects.get(pk=id)
    eliminarAlumno.delete()
    return redirect ('mostrarAlumnosCoorte')
# --------------------

# ----------ESTADO----------
def estadoCrearFormulario (request, id):
    formulario= estadoForm()
    if id != 0:
        registro=Estado.objects.get(pk=id)
        formulario.fields['id'].initial=registro.id
        formulario.fields['descripcion'].initial=registro.descripcion
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarestado.html', {'form':formulario})

def guardarEstado(request):
    if request.method=='POST':
       if request.POST['id']>'0':
            xid=request.POST['id']
            registro=Estado.objects.get(pk=xid)
            registro.descripcion=request.POST['descripcion']
            registro.save()
           
       else:
            respuesta=request.POST['descripcion']
            registro=Estado(descripcion=respuesta)
            registro.save()
           
    return redirect ('estados')

def consultarEstado (request):
    planilla=Estado.objects.all().order_by("descripcion")
    return render (request,"estado.html",{"estados":planilla})

def estadoEliminar (request, id):
    try: 
        registro1 = Estado.objects.get(pk=id)
        registro1.delete()
        return redirect ('estados')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+registro1.descripcion+ ',tiene registros anexados')
        return redirect ('estados') 

# --------------------

# ----------GENERO----------
def generoCrearFormulario (request, id):
    formulario= generoForm() #traigo formulario vacio
    if id != 0:
        registro=Genero.objects.get(pk=id) #trae el registro en cuestion
        formulario.fields['id'].initial=registro.id
        formulario.fields['descripcion'].initial=registro.descripcion
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregargenero.html', {'form':formulario})

def generoGuardar(request):
    if request.method=='POST':
        if int(request.POST['id'])>0: #editamos
            xid=request.POST['id']
            registro=Genero.objects.get(pk=xid)
            registro.descripcion=request.POST['descripcion']
        else:
            respuesta=request.POST['descripcion']
            registro=Genero(descripcion=respuesta)
        registro.save()
    return redirect('genero')


def consultarGenero (request):
    generos = Genero.objects.all().order_by('descripcion')
    return render (request, "genero.html",{"generos":generos})

def generoEliminar (request, id):
    try: 
        eliminarGenero1 = Genero.objects.get(pk=id)
        eliminarGenero1.delete()
        return redirect ('genero')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarGenero1.descripcion+ ',tiene registros anexados')
        return redirect ('genero') 
# --------------------

# ----------COORTE----------
def consultarCoorte(request):
    Coortes=Carreraxcoorte.objects.all().order_by('id')
    return render (request, "coorte.html",{"coortes":Coortes})

def coorteCrearFormulario (request, id):
    formulario= coorteForm()
    carrera=Carrera.objects.all().order_by('nombre')
    if id != 0:
        coorte1=Carreraxcoorte.objects.get(pk=id)
        formulario.fields['id'].initial=coorte1.Coorte_id.id
        formulario.fields['fechaInicio'].initial=coorte1.Coorte_id.ano_ini
        formulario.fields['fechaFin'].initial=coorte1.Coorte_id.ano_fin
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarcoorte.html', {'form':formulario, 'carreras':carrera })

def coorteGuardar(request):
    if request.method=='POST':
        xid=request.POST['id']
        fechaInicio=request.POST['fechaInicio']
        fechaFin=request.POST['fechaFin']
        carrera_id=request.POST['carreraid']
        carreras=Carrera.objects.get(pk=carrera_id)
        registro=Coorte()
        registro.ano_ini=fechaInicio
        registro.ano_fin=fechaFin
        registro.save()
        carreraxcohorte1=Carreraxcoorte()
        carreraxcohorte1.carrera_id=carreras
        carreraxcohorte1.Coorte_id=registro
        carreraxcohorte1.save()
    return redirect ('coortes')

def coorteEliminar (request, id):
    try: 

        eliminarCoorte1 = Carreraxcoorte.objects.get(pk=id)
        eliminarCoorte1.delete()
        return redirect ('coortes')
    except ProtectedError as e:
        messages.info(request, 'Error al eliminar '+eliminarCoorte1.nombre+ ', tiene registros anexados')
        return redirect ('coortes') 
    
def mostrarAlumno(request, id):
    objetoCXC = Carreraxcoorte.objects.get(pk = id)
    listaAlumnos = AlumnosxCarreraxcoorte.objects.filter(
        Carreraxcoorte_id = objetoCXC
)
    return render (request, 'mostrarAlumnosCoorte.html',{'listaAlumnos':listaAlumnos,'coorte':objetoCXC})

def eliminarAlumnoCoorte (request, id, idcoorte):
    try: 
        alumno1 = Alumnos.objects.get(pk=id)
        coorte1 = Carreraxcoorte.objects.get(pk=idcoorte)
        alumnosPorCoorte = AlumnosxCarreraxcoorte.objects.filter(Alumnos_id=alumno1
                                                                ).filter(Carreraxcoorte_id=coorte1)
        for alumnos in alumnosPorCoorte:
            alumnos.delete()
        return redirect ('mostrarAlumnosCoorte', id=idcoorte)
    except ProtectedError as e:
        eliminarAlumno1 = AlumnosxCarreraxcoorte.objects.get(pk=id)
        messages.info(request, 'Error al eliminar '+eliminarAlumno1.Apellido+', '+eliminarAlumno1.Nombres+ ', tiene registros anexados')
        return redirect ('mostrarAlumnosCoorte', id=idcoorte)
    
def agregarAlumnoCoorte (request):
    listaAlumnos = Alumnos.objects.all().order_by('Apellido')
    return render(request, "agregaralumnoscoorte.html", {"alumnos":listaAlumnos})

def cargarAlumno (request):
    if request.method == 'GET':
        alumno=request.GET['id']
        alumnoSeleccionado = Alumnos.objects.filter(id=alumno)
        return JsonResponse(list(alumnoSeleccionado.values('id', 'Apellido', 'Nombres', 'Genero_id__descripcion', 'LocalidadVive_id__nombre', 'Telefono', 'Email' )), safe=False)

def guardarNuevoAlumnoCoorte(request):
    if request.method=='GET':
        idCoorte = request.GET['carreraDeLaCoorte']
        carrera = Carreraxcoorte.objects.get(pk=idCoorte)
        estado = Estado.objects.get(pk=1)
        n = int(request.GET['cantidadAlumnosNuevos'])
        for i in range (n):
            alumno = Alumnos.objects.get(pk=request.GET['registro'+str(i)])
            objetoAlumno = AlumnosxCarreraxcoorte(
                Alumnos_id = alumno,
                Carreraxcoorte_id = carrera,
                Estado_id = estado
            )
            objetoAlumno.save()
    return redirect('mostrarAlumnosCoorte', id=idCoorte)

def traerEstados(request):
    estados = Estado.objects.all().order_by('descripcion')
    return JsonResponse(list(estados.values('id', 'descripcion')),safe=False)

def guardarEstadoAlumnoCoorte(request):
    if request.method=='GET':
        objetoEstado = Estado.objects.get(pk=request.GET['idEstado'])
        objetoAlumno = AlumnosxCarreraxcoorte.objects.get(pk=request.GET['idAlumno'])
        objetoAlumno.Estado_id=objetoEstado
        objetoAlumno.save()
        objetoAlumno = AlumnosxCarreraxcoorte.objects.values('Alumnos_id__Nombres', 'Alumnos_id__Apellido', 'Estado_id__descripcion', 'Estado_id').filter(id=request.GET['idAlumno'])
        return JsonResponse(list(objetoAlumno[0]),safe=False)
# --------------------

# ----------RANGOSEDADES----------

def consultarRangos (request):
    Cursor1 = Rangosedades.objects.all()
    return render (request, "rangosedades.html",{"listaderangos":Cursor1})

def agregarRangosEdades (request, id):
    formulario= rangosEdadesForm()
    if id != 0:
        rangos1=Rangosedades.objects.get(pk=id)
        formulario.fields['id'].initial=rangos1.id
        formulario.fields['desde'].initial=rangos1.desde
        formulario.fields['hasta'].initial=rangos1.hasta
    else:
        formulario.fields['id'].initial=0
    return render (request, 'agregarRangos.html', {'form':formulario})

def guardarRangosEdades(request):
    if request.method=='POST':
        xid=request.POST['id']
        desde=request.POST['desde']
        hasta=request.POST['hasta']
        if int(request.POST['id'])>0:
            registro=Rangosedades.objects.get(pk=xid)
        else:
            registro=Rangosedades()
    registro.desde=desde
    registro.hasta=hasta
    registro.save()
    return redirect ('Rangos')
 
def rangoEdadesEliminar (request, id):
    try: 
        eliminarRango1 = Rangosedades.objects.get(pk=id)
        eliminarRango1.delete()
        return redirect ('Rangos')
    except ProtectedError as e:
        messages.info(request, 'Error al eliminar '+eliminarRango1.nombre+ ',tiene registros anexados')
        return redirect ('Rangos') 
# --------------------
#-----------TIPODECARRERA------------
def consultarTipodeCarrera (request):
    tipodeCarrera1 = Tipodecarrera.objects.all().order_by('descripcion')
    return render (request,"tipodecarrera.html",{'tipodecarrera':tipodeCarrera1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
   
def tipodeCarreraCrearFormulario (request, id):
    Formulario= tipodeCarreraForm()
    if id !=0:
        tipodecarrera1=Tipodecarrera.objects.get(pk=id)
        Formulario.fields['id'].initial = tipodecarrera1.id
        Formulario.fields['descripcion'].initial=tipodecarrera1.descripcion
    else:
        Formulario.fields['id'].initial=0
    return render (request, 'agregartipodecarrera.html', {'form':Formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso carrera ---

def guardarTipodeCarrera(request):
    if request.method=='POST':
        xid=request.POST['id']
        descripcion=request.POST['descripcion']
        if int(request.POST['id'])>0:
            registro=Tipodecarrera.objects.get(pk=xid)
        else:
            registro=Tipodecarrera()
    registro.descripcion=request.POST['descripcion']      
    registro.save()
    return redirect ('tipodecarrera')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario una carrera en especifico ---

def tipodeCarreraEliminar (request, id):
    try: 

        eliminartipodeCarrera1 = Tipodecarrera.objects.get(pk=id)
        eliminartipodeCarrera1.delete()
        return redirect ('tipodecarrera')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminartipodeCarrera1.descripcion+ ',tiene registros anexados')
        return redirect ('tipodecarrera') 
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---
    
# --------------------
#--------MODALIDADDEDICTADO-------
def consultarModalidaddeDictado (request):
    Modalidad1 = Modalidaddedictado.objects.all().order_by('descripcion')
    return render (request,"modalidaddedictado.html",{'modalidaddedictado':Modalidad1})
# --- Esta definicion o funcion sirve para realizar la consulta de un registro determinado ---
   
def modalidaddeDictadoCrearFormulario (request, id):
    Formulario= modalidaddeDictadoForm()
    if id !=0:
        Modalidad1=Modalidaddedictado.objects.get(pk=id)
        Formulario.fields['id'].initial = Modalidad1.id
        Formulario.fields['descripcion'].initial=Modalidad1.descripcion
    else:
        Formulario.fields['id'].initial=0
    return render (request, 'agregarmodalidaddedictado.html', {'form':Formulario})
# --- Esta definicion o funcion sirve para crear el formulario deseado, en este caso carrera ---

def guardarModalidaddeDictado(request):
    if request.method=='POST':
        xid=request.POST['id']
        descripcion=request.POST['descripcion']
        if int(request.POST['id'])>0:
            registro=Modalidaddedictado.objects.get(pk=xid)
        else:
            registro=Modalidaddedictado()
    registro.descripcion=request.POST['descripcion']      
    registro.save()
    return redirect ('modalidaddedictado')
#--- Esta definicion o funcion sirve para guardar o modificar en el formulario una carrera en especifico ---

def modalidaddeDictadoEliminar (request, id):
    try: 

        eliminarmodalidad1 = Modalidaddedictado.objects.get(pk=id)
        eliminarmodalidad1.delete()
        return redirect ('modalidaddedictado')
    except ProtectedError as e:
        messages.info(request, 'Error en eliminar '+eliminarmodalidad1.descripcion+ ',tiene registros anexados')
        return redirect ('modalidaddedictado') 
# --- Esta definicion o funcion sirve para realizar la eliminacion de un registro en especifico ---
    
# --------------------
def estadistica (request):
    cantidades=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre','Carreraxcoorte_id__Coorte_id__ano_ini').annotate(cantidad=Count('Carreraxcoorte_id'))
    cantixcarrera=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre').annotate(cantidad=Count('Carreraxcoorte_id__carrera_id'))
 
    lista=[]
    listageneros=[]
    listatotalgenero=[]
    listaprovincia=[]
    listaalumnosxprovincia=[]
    EDADES=[17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
    listaedades=[]
    listaedadesxcarrera=[]
    Carreras = Carrera.objects.all()
    Estados = Estado.objects.get(pk=1)
    cantidadtotal = 0
    a=0
    b=0
    c=0
    for i in Carreras: 
    
        CantidadAlumnos = AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Estado_id = Estados
                                                                ).annotate(cantidad=Count('id'))

        
        if CantidadAlumnos:
                                     
            cantidadtotal = cantidadtotal + CantidadAlumnos[0]['cantidad']
            lista.append(CantidadAlumnos)
            
        
        Generos=Genero.objects.all()
        for g in Generos:
            ConteoGenero=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre',
                                                                'Alumnos_id__Genero_id__descripcion'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Alumnos_id__Genero_id=g
                                                                ).filter(Estado_id = Estados
                                                                ).annotate(cantidad=Count('id'))
            listageneros.append(ConteoGenero)
            
        provincia1=Provincia.objects.all()
        for e in provincia1:
            cantProvincias=AlumnosxCarreraxcoorte.objects.values('Alumnos_id__LocalidadNac_id__departamento_id__provincia_id__nombre',
                                                                 'Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Alumnos_id__LocalidadNac_id__departamento_id__provincia_id=e                                                           
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Estado_id = Estados
                                                                ).annotate(cantidad=Count('id'))
            listaprovincia.append(cantProvincias)
            
        for n in EDADES:
            if n == 17:
                Fechaedad= averiguarFecha(17)
                dia=Fechaedad.day
                mes=Fechaedad.month
                ano=Fechaedad.year
                fechaH=datetime.today()
                hoy=str(fechaH.year)+"-"+str(fechaH.month)+"-"+str(fechaH.day)
                
                
                cantEdad=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i                                                                                                    
                                                                ).filter(Estado_id = Estados
                                                                ).filter(Alumnos_id__Fechanac__range=[str(ano)+"-"+str(mes)+"-"+str(dia),hoy]  
                                                                ).annotate(cantidad=Count('id'))                                                  
            elif n == 30:
                Fechaedad= averiguarFecha(n)
                dia=Fechaedad.day
                mes=Fechaedad.month
                ano=Fechaedad.year
                
               
                cantEdad=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i                                                    
                                                                ).filter(Estado_id = Estados
                                                                ).filter(Alumnos_id__Fechanac__range=["1900-01-01",str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                                ).annotate(cantidad=Count('id'))                                               
            else:
                Fechaedad= averiguarFecha(n)
                dia=Fechaedad.day
                mes=Fechaedad.month
                ano=Fechaedad.year
                
               
                Fechaedad2= Fechaedad - relativedelta(years=1) + relativedelta(days=1) 
                
                cantEdad=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i                                                                     
                                                                ).filter(Estado_id = Estados
                                                                ).filter(Alumnos_id__Fechanac__range=[Fechaedad2,str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                                ).annotate(cantidad=Count('id'))    
            listaedadesxcarrera.append({'resultado':cantEdad,'Edad':n}) 
          
    for n in EDADES:
        if n == 17:
            Fechaedad= averiguarFecha(17)
            dia=Fechaedad.day
            mes=Fechaedad.month
            ano=Fechaedad.year
            fechaH=datetime.today()
            hoy=str(fechaH.year)+"-"+str(fechaH.month)+"-"+str(fechaH.day)
            
            
            canttotalEdad=AlumnosxCarreraxcoorte.objects.values('Estado_id'
                                                            ).filter(Estado_id = Estados
                                                            ).filter(Alumnos_id__Fechanac__range=[str(ano)+"-"+str(mes)+"-"+str(dia),hoy]  
                                                            ).annotate(cantidad=Count('id'))                                                  
        elif n == 30:
            Fechaedad= averiguarFecha(n)
            dia=Fechaedad.day
            mes=Fechaedad.month
            ano=Fechaedad.year
            
            
            canttotalEdad=AlumnosxCarreraxcoorte.objects.values('Estado_id'
                                                            ).filter(Estado_id = Estados
                                                            ).filter(Alumnos_id__Fechanac__range=["1900-01-01",str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                            ).annotate(cantidad=Count('id'))                                               
        else:
            Fechaedad= averiguarFecha(n)
            dia=Fechaedad.day
            mes=Fechaedad.month
            ano=Fechaedad.year
            
           
            Fechaedad2= Fechaedad - relativedelta(years=1) + relativedelta(days=1) 
            
            canttotalEdad=AlumnosxCarreraxcoorte.objects.values('Estado_id'
                                                            ).filter(Estado_id = Estados
                                                            ).filter(Alumnos_id__Fechanac__range=[Fechaedad2,str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                            ).annotate(cantidad=Count('id'))    
        listaedades.append({'resultado':canttotalEdad,'Edad':n})    
    print(listaedades)
    
    Genero1=Genero.objects.all()
    for l in Genero1: 
        cantidadxGenero=AlumnosxCarreraxcoorte.objects.values('Alumnos_id__Genero_id__descripcion'
                                                            ).filter(Alumnos_id__Genero_id=l
                                                            ).filter(Estado_id = Estados
                                                            ).annotate(cantidad=Count('id')) 
        listatotalgenero.append(cantidadxGenero)     
        
        
    Alumnosxprovincia=Provincia.objects.all()
    for p in Alumnosxprovincia:
        cantidadxProvincia=AlumnosxCarreraxcoorte.objects.values('Alumnos_id__LocalidadNac_id__departamento_id__provincia_id__nombre'                                                           
                                                             ).filter(Alumnos_id__LocalidadNac_id__departamento_id__provincia_id=p                                                         
                                                             ).filter(Estado_id = Estados
                                                             ).annotate(cantidad=Count('id'))
        listaalumnosxprovincia.append(cantidadxProvincia)
                    
    return render (request,"estadistica.html",{'cantidades':lista,'CantidadTotal':cantidadtotal,'Listageneros':listageneros,'ListatotalGenero':listatotalgenero,'listaAlumnosxProvincia':listaalumnosxprovincia,'ListaProvincia':listaprovincia,'Listaedades':listaedades,'ListaedadesXcarrera':listaedadesxcarrera})

#--------------------

def estadisticaPrimero (request):
    cantidades=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre','Carreraxcoorte_id__Coorte_id__ano_ini').annotate(cantidad=Count('Carreraxcoorte_id'))
    cantixcarrera=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre').annotate(cantidad=Count('Carreraxcoorte_id__carrera_id'))
 
    lista=[]
    listageneros=[]
    listatotalgenero=[]
    listaprovincia=[]
    listaalumnosxprovincia=[]
    EDADES=[17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30]
    listaedades=[]
    listaedadesxcarrera=[]
    
    hoy=datetime.today()
    ano=str(hoy.year)
    
    Carreras = Carrera.objects.all()
    Estados = Estado.objects.get(pk=1)
    cantidadtotal = 0
    a=0
    b=0
    c=0
    for i in Carreras: 
    
        CantidadAlumnos = AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]         
                                                                ).filter(Estado_id = Estados
                                                                ).annotate(cantidad=Count('id'))
        
        if CantidadAlumnos:
                                     
            cantidadtotal = cantidadtotal + CantidadAlumnos[0]['cantidad']
            lista.append(CantidadAlumnos)
            
        
        Generos=Genero.objects.all()
        for g in Generos:
            ConteoGenero=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre',
                                                                'Alumnos_id__Genero_id__descripcion'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]        
                                                                ).filter(Alumnos_id__Genero_id=g
                                                                ).filter(Estado_id = Estados
                                                                ).annotate(cantidad=Count('id'))
            listageneros.append(ConteoGenero)
            
        provincia1=Provincia.objects.all()
        for e in provincia1:
            cantProvincias=AlumnosxCarreraxcoorte.objects.values('Alumnos_id__LocalidadNac_id__departamento_id__provincia_id__nombre',
                                                                 'Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Alumnos_id__LocalidadNac_id__departamento_id__provincia_id=e                                                           
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]        
                                                                ).filter(Estado_id = Estados
                                                                ).annotate(cantidad=Count('id'))
            listaprovincia.append(cantProvincias)
            
        for n in EDADES:
            if n == 17:
                Fechaedad= averiguarFecha(17)
                dia=Fechaedad.day
                mes=Fechaedad.month
                ano=Fechaedad.year
                fechaH=datetime.today()
                hoy=str(fechaH.year)+"-"+str(fechaH.month)+"-"+str(fechaH.day)
                
                
                cantEdad=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i  
                                                                ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]                                                                                                         
                                                                ).filter(Estado_id = Estados
                                                                ).filter(Alumnos_id__Fechanac__range=[str(ano)+"-"+str(mes)+"-"+str(dia),hoy]  
                                                                ).annotate(cantidad=Count('id'))                                                  
            elif n == 30:
                Fechaedad= averiguarFecha(n)
                dia=Fechaedad.day
                mes=Fechaedad.month
                ano=Fechaedad.year
                
               
                cantEdad=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i
                                                                ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]                                                             
                                                                ).filter(Estado_id = Estados
                                                                ).filter(Alumnos_id__Fechanac__range=["1900-01-01",str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                                ).annotate(cantidad=Count('id'))                                               
            else:
                Fechaedad= averiguarFecha(n)
                dia=Fechaedad.day
                mes=Fechaedad.month
                ano=Fechaedad.year
                
               
                Fechaedad2= Fechaedad - relativedelta(years=1) + relativedelta(days=1) 
                
                cantEdad=AlumnosxCarreraxcoorte.objects.values('Carreraxcoorte_id__carrera_id__nombre'
                                                                ).filter(Carreraxcoorte_id__carrera_id=i  
                                                                ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]                                                                            
                                                                ).filter(Estado_id = Estados
                                                                ).filter(Alumnos_id__Fechanac__range=[Fechaedad2,str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                                ).annotate(cantidad=Count('id'))    
            listaedadesxcarrera.append({'resultado':cantEdad,'Edad':n}) 
          
    for n in EDADES:
        if n == 17:
            Fechaedad= averiguarFecha(17)
            dia=Fechaedad.day
            mes=Fechaedad.month
            ano=Fechaedad.year
            fechaH=datetime.today()
            hoy=str(fechaH.year)+"-"+str(fechaH.month)+"-"+str(fechaH.day)
            
            
            canttotalEdad=AlumnosxCarreraxcoorte.objects.values('Estado_id'
                                                            ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]   
                                                            ).filter(Estado_id = Estados
                                                            ).filter(Alumnos_id__Fechanac__range=[str(ano)+"-"+str(mes)+"-"+str(dia),hoy]  
                                                            ).annotate(cantidad=Count('id'))                                                  
        elif n == 30:
            Fechaedad= averiguarFecha(n)
            dia=Fechaedad.day
            mes=Fechaedad.month
            ano=Fechaedad.year
            
            
            canttotalEdad=AlumnosxCarreraxcoorte.objects.values('Estado_id'
                                                            ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]   
                                                            ).filter(Estado_id = Estados
                                                            ).filter(Alumnos_id__Fechanac__range=["1900-01-01",str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                            ).annotate(cantidad=Count('id'))                                               
        else:
            Fechaedad= averiguarFecha(n)
            dia=Fechaedad.day
            mes=Fechaedad.month
            ano=Fechaedad.year
            
           
            Fechaedad2= Fechaedad - relativedelta(years=1) + relativedelta(days=1) 
            
            canttotalEdad=AlumnosxCarreraxcoorte.objects.values('Estado_id'
                                                            ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]   
                                                            ).filter(Estado_id = Estados
                                                            ).filter(Alumnos_id__Fechanac__range=[Fechaedad2,str(ano)+"-"+str(mes)+"-"+str(dia)] 
                                                            ).annotate(cantidad=Count('id'))    
        listaedades.append({'resultado':canttotalEdad,'Edad':n})    
    print(listaedades)
    
    Genero1=Genero.objects.all()
    for l in Genero1: 
        cantidadxGenero=AlumnosxCarreraxcoorte.objects.values('Alumnos_id__Genero_id__descripcion'
                                                            ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]  
                                                            ).filter(Alumnos_id__Genero_id=l
                                                            ).filter(Estado_id = Estados
                                                            ).annotate(cantidad=Count('id')) 
        listatotalgenero.append(cantidadxGenero)     
        
        
    Alumnosxprovincia=Provincia.objects.all()
    for p in Alumnosxprovincia:
        cantidadxProvincia=AlumnosxCarreraxcoorte.objects.values('Alumnos_id__LocalidadNac_id__departamento_id__provincia_id__nombre'  
                                                             ).filter(Carreraxcoorte_id__Coorte_id__ano_ini__range=[str(ano)+"-1-1",str(ano)+"-12-31"]                                                             
                                                             ).filter(Alumnos_id__LocalidadNac_id__departamento_id__provincia_id=p                                                         
                                                             ).filter(Estado_id = Estados
                                                             ).annotate(cantidad=Count('id'))
        listaalumnosxprovincia.append(cantidadxProvincia)
                    
    return render (request,"estadisticaprimero.html",{'cantidades':lista,'CantidadTotal':cantidadtotal,'Listageneros':listageneros,'ListatotalGenero':listatotalgenero,'listaAlumnosxProvincia':listaalumnosxprovincia,'ListaProvincia':listaprovincia,'Listaedades':listaedades,'ListaedadesXcarrera':listaedadesxcarrera})

def filtrarBusqueda (request):
    if request.method=='GET':
        seleccion=request.GET['filtro']
        print(seleccion)
        if seleccion=='1':
           Alumnos1=Alumnos.objects.filter(Documento=request.GET['Filtrar'])
           print(Alumnos1)
        else:
           Alumnos1=Alumnos.objects.filter(Apellido__icontains=request.GET['Filtrar'])  
           print(Alumnos1)  

        return render (request,"alumnos.html",{"alumnos":Alumnos1})
    else: 
        Alumnos1=Alumnos.objects.all()
        print(Alumnos1)
        return render (request,"alumnos.html",{"alumnos":Alumnos1})       
