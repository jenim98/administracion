function traerCarrera(id) {
    datosAnteriores = $('#resultado').html()
    carrera = $('#' + id).text()
    fecha = $('#id_coorte option:selected').text()
    datos = [
        '<tr id="tr"+id>',
            '<td hidden>{{alumno.Alumnos_id.id}}</td>',
            '<td>'+fecha+'</td>',
            '<td>'+carrera+'</td>',
            '<td><a onclick="eliminarCarrera(id)"><i style="color: #000000; cursor:pointer;" class="fa-solid fa-trash-can"></i></a></td>',
        '</tr>'
    ].join()
    datosActuales = datosAnteriores + datos
    $('#resultado').html(datosActuales)
}

function eliminarCarrera(id) {
    $('#tr'+id).remove()
}

function guardar() {
    i = 0;
    $('#resultado tr').each(function(index) {
        $(this).find(":input").prop('name','registro'+i);
        i = i + 1;
    })
    $('#cantidad').val(i);
    let error = 0;
    if($('#id_localidadNacimiento').val()==""){
        error = 1;
        $('#id_localidadNacimiento').css(
            {'border-color' : 'red'}
        )
    }
    if($('#id_localidadResidencia').val()==""){
        error = 1;
        $('#id_localidadResidencia').css(
            {'border-color' : 'red'}
        )
    }
    if($('#id_TipoDocumento').val()==""){
        error = 1;
        $('#id_TipoDocumento').css(
            {'border-color' : 'red'}
        )
    }
    if($('#id_genero').val()==""){
        error = 1;
        $('#id_genero').css(
            {'border-color' : 'red'}
        )
    }
    if($('#id_fechaNacimiento').val()==""){
        error = 1;
        $('#id_fechaNacimiento').css(
            {'border-color' : 'red'}
        )
    }
    if(error == 1){
        alert("Faltan completar datos");
    }
    else{
        $('#cargarAlumno').submit();
    }
}