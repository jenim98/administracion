"""tresg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from isbh import views as gestion
from materias import views as Materia
from django.contrib.auth.views import *
urlpatterns = [
# ----------GENERALES----------
    path('inicio/', gestion.principal, name='inicio'),
    path('correlatividad/', gestion.correlatividad, name='correlatividad'),
# --------------------

# ----------USUARIO----------
path('',LoginView.as_view()),
path('o/', LoginView.as_view()),

path('login/', LoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
path('admin/', admin.site.urls),
path('accounts/', include('django.contrib.auth.urls')),
# --------------------

# ----------PAIS----------
    path('pais/', gestion.consultarPais, name='pais'),
    path('pais/crearpais/<int:id>', gestion.paisCrearFormulario, name='nuevopais'),
    path('pais/guardarPais/', gestion.guardarPais, name='guardarPais'),
    path('pais/eliminarpais/<int:id>', gestion.paisEliminar, name= 'eliminarPais'),
# --------------------

# ----------TIPODOC----------
    path('tipodoc/creartipodoc/<int:id>', gestion.tipodocCrearFormulario, name='nuevotipo'),
    path('tipodoc/guardartipodoc/', gestion.guardarTipodoc, name='guardarTipodoc'), 
    path('tipodoc/', gestion.consultarTipodoc, name='tipo'),
    path('tipodoc/eliminarTipodoc/<int:id>', gestion.tipodocEliminar, name= 'eliminarTipodoc'),
# --------------------

# ----------LOCALIDAD----------
    path('localidad/',gestion.consultarLocalidad, name='localidad'),
    path('localidad/crearlocalidad/<int:id>', gestion.localidadCrearFormulario, name='nuevaLocalidad'),
    path('localidad/guardarlocalidad/', gestion.localidadGuardar, name='guardarLocalidad'),
    path('localidad/eliminarlocalidad/<int:id>', gestion.localidadEliminar, name= 'eliminarLocalidad'),
# --------------------

# ----------CARRERA----------
    path('carrera/consultarCarrera/', gestion.consultarCarrera, name='carrera'),
    path('carrera/crearCarrera/<int:id>', gestion.carreraCrearFormulario, name='nuevaCarrera'),
    path('carrera/guardarCarrera/', gestion.guardarCarrera, name='guardarCarrera'),
    path('carrera/eliminarCarrera/<int:id>', gestion.carreraEliminar, name= 'eliminarCarrera'),

# --------------------

# ----------PROVINCIA----------
    path('provincia/',gestion.consultarProvincia,name='provincia'),
    path('provincia/crearprovincia/<int:id>', gestion.provinciaCrearformulario, name='nuevaprovincia'),
    path('provincia/guardarprovincia/', gestion.provinciaGuardar, name='guardarprovincia'),
    path('provincia/cargarProvincia/', gestion.cargarProvincia, name='cargarProvincia'),
    path('provincia/eliminarProvincia/<int:id>', gestion.provinciaEliminar, name= 'eliminarProvincia'),
# --------------------

# ----------DEPARTAMENTO----------
    path('departamento/',gestion.consultarDepartamento,name="departamento"),
    path('departamento/creardepartamento/<int:id>', gestion.departamentoCrearFormulario, name='nuevoDepartamento'),
    path('departamento/guardardepartamento/', gestion.guardarDepartamento, name='guardarDepartamento'), 
    path('departamento/cargarDepartamentos/', gestion.cargarDepartamento, name='cargarDepartamentos'),
    path('departamento/eliminarDepartamento/<int:id>', gestion.departamentoEliminar, name= 'eliminarDepartamento'),
# --------------------

# ----------GENERO----------
    path('genero/',gestion.consultarGenero, name='genero'),
    path('genero/creargenero/<int:id>', gestion.generoCrearFormulario, name='nuevoGenero'),
    path('genero/guardargenero/', gestion.generoGuardar, name='guardarGenero'),
    path('genero/eliminargenero/<int:id>', gestion.generoEliminar, name= 'eliminarGenero'),
# --------------------

# ----------ALUMNOS----------
    path('alumnos/',gestion.consultarAlumnos, name='alumno'),
    path('alumnos/crearalumnos/<int:id>', gestion.alumnosCrearFormulario, name='nuevoAlumno'),
    path('alumnos/guardaralumnos/', gestion.guardarAlumnos, name='guardarAlumnos'),
    path('alumnos/traerlocalidad/',gestion.traerLocalidad, name='traerLocalidad'),
    path('alumnos/eliminaralumnos/<int:id>', gestion.alumnosEliminar, name= 'eliminarAlumno'),
    path('traerfecha/', gestion.traerFecha, name='traerfecha'),
    path('cargarcarreraxcoorte/', gestion.cargarCarreraxCoorte, name='cargarCarreraxCoorte'),
    path('estadistica/', gestion.estadistica, name='estadistica'),
    path('estadisticaprimero/', gestion.estadisticaPrimero, name='EstadisticaPrimero'),
    path('alumnos/filtrar/', gestion.filtrarBusqueda, name='filtrarbusqueda'),
# --------------------

# ----------ESTADO----------
    path('estado/',gestion.consultarEstado,name="estados"),
    path('estado/crearestado/<int:id>', gestion.estadoCrearFormulario,name='nuevoEstado'),
    path('estado/guardarestado/', gestion.guardarEstado,name="guardarEstado"),
    path('estado/eliminarestado/<int:id>', gestion.estadoEliminar, name= 'eliminarEstado'),
# --------------------

# ----------COORTE----------
    path('coorte/',gestion.consultarCoorte,name="coortes"),
    path('coorte/crearcoorte/<int:id>', gestion.coorteCrearFormulario, name='nuevoCoorte'),
    path('coorte/guardarcoorte/', gestion.coorteGuardar, name='guardarCoorte'),
    path('coorte/eliminarcoorte/<int:id>', gestion.coorteEliminar, name= 'eliminarCoorte'),
    path('coorte/mostrarAlumnosCoorte/<int:id>', gestion.mostrarAlumno, name='mostrarAlumnosCoorte'),
    path('coorte/eliminarAlumnoCoorte/<int:id>/<int:idcoorte>', gestion.eliminarAlumnoCoorte, name='eliminarAlumnoCoorte'),
    path('coorte/agregarAlumnoCoorte/', gestion.agregarAlumnoCoorte, name='agregarAlumnoCoorte'),
    path('coorte/cargarAlumno/', gestion.cargarAlumno, name='cargarAlumno'),
    path('coorte/eliminarAlumnoCoorte/<int:id>', gestion.eliminarAlumnoCoorte, name= 'eliminarAlumnoCoorte'),
    path('coorte/guardarNuevoAlumnoCoorte/', gestion.guardarNuevoAlumnoCoorte, name='guardarNuevoAlumnoCoorte'),
    path('coorte/traerEstados/', gestion.traerEstados, name='traerEstados'),
    path('coorte/guardarEstadoAlumnoCoorte/', gestion.guardarEstadoAlumnoCoorte, name='guardarEstadoAlumnoCoorte'),
# --------------------

# ---------RANGOEDADES----------
    path('rangosedades/', gestion.consultarRangos,name="Rangos"),
    path('rangosedades/agregarrangosedades/<int:id>', gestion.agregarRangosEdades, name='AgregarRangos'),
    path('rangosedades/guardarrangosedades/', gestion.guardarRangosEdades, name='GuardarRangos'),
    path('rangosedades/eliminarrangoedades/<int:id>', gestion.rangoEdadesEliminar, name= 'eliminarRango'),
# --------------------

#---------TIPODECARRERA--------
    path('tipodecarrera/consultarTipodeCarrera/', gestion.consultarTipodeCarrera, name='tipodecarrera'),
    path('tipodecarrera/crearTipodeCarrera/<int:id>', gestion.tipodeCarreraCrearFormulario, name='nuevoTipodeCarrera'),
    path('tipodecarrera/guardarTipodeCarrera/', gestion.guardarTipodeCarrera, name='guardarTipodeCarrera'),
    path('tipodecarrera/eliminarTipodeCarrera/<int:id>', gestion.tipodeCarreraEliminar, name= 'eliminarTipodeCarrera'),
#--------------  
  
#--------MODALIDADDEDICTADO--------
    path('modalidaddedictado/constarModalidaddedictado/', gestion.consultarModalidaddeDictado, name='modalidaddedictado'),
    path('modalidaddedictado/crearModalidaddedictado/<int:id>', gestion.modalidaddeDictadoCrearFormulario, name='nuevaModalidaddedictado'),
    path('modalidaddedictado/guardarModalidaddedictado/', gestion.guardarModalidaddeDictado, name='guardarModalidaddedictado'),
    path('modalidaddedictado/eliminarModalidaddedictado/<int:id>', gestion.modalidaddeDictadoEliminar, name= 'eliminarModalidaddedictado'),
#---------------
# URL DE LA APLICACION MATERIA
#-------CURSOS-------
    path('cursos/constarCursos/', Materia.consultarCurso, name='cursos'),
    path('cursos/crearCursos/<int:id>', Materia.cursosCrearFormulario, name='nuevocurso'),
    path('cursos/guardarCursos/', Materia.guardarCursos, name='guardarcursos'),
    path('cursos/eliminarCursos/<int:id>', Materia.cursosEliminar, name= 'eliminarCursos'),
#---------------

#-------MATERIAS-------
    path('materias/constarMateria/<int:id>', Materia.consultarMaterias, name='materias'),
    path('materias/crearMateria/<int:id>/<int:idcarrera>', Materia.materiasCrearFormulario, name='nuevaMateria'),
    path('materias/guardarMateria/', Materia.guardarMaterias, name='guardarMaterias'),
    path('materias/eliminarMateria/<int:id>/<int:idcarrera>', Materia.materiasEliminar, name= 'eliminarMaterias'),
    
#--------
#---------PROFESORES-----
    path('profesores/',Materia.consultarProfesores, name='profesor'),
    path('profesores/crearprofesores/<int:id>', Materia.profesoresCrearFormulario, name='nuevoProfesor'),
    path('profesores/guardarprofesores/', Materia.guardarProfesores, name='guardarProfesores'),
    path('profesores/traerlocalidad/',Materia.traerLocalidad, name='traerLocalidad'),
    path('profesores/eliminarprofesores/<int:id>', Materia.profesoresEliminar, name= 'eliminarProfesor'),

#--------MODODERENDIR--------
    path('mododerendir/constarMododerendir/', Materia.consultarMododerendir, name='mododerendir'),
    path('mododerendir/crearMododerendir/<int:id>', Materia.mododerendirCrearFormulario, name='nuevoMododerendir'),
    path('mododerendir/guardarMododerendir/', Materia.guardarMododerendir, name='guardarMododerendir'),
    path('mododerendir/eliminarMododerendir/<int:id>', Materia.mododerendirEliminar, name= 'eliminarMododerendir'),
#---------------
]