function traerCarrera(id) {
    datosAnteriores = $('#resultado').html()
    carrera = $('#' + id).text()
    fecha = $('#id_coorte option:selected').text()
    datos = [
        '<tr id="tr"+id>',
            '<td hidden><input hidden value="'+id+'"></td>',
            '<td>'+fecha+'</td>',
            '<td>'+carrera+'</td>',
            '<td><a title="Eliminar carrera" onclick="eliminarCarrera(id)"><i style="color: #000000; cursor:pointer;" class="fa-solid fa-trash-can"></i></a></td>',
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
    console.log($('#resultado').html())
    $('#cantidad').val(i);
    console.log($('#cantidad').val())
    let error = 0;
    if($('#id_localidadNacimiento').val()==""){
        error = 1;
        
    }
    if($('#id_localidadResidencia').val()==""){
        error = 1;
        
    }
    if($('#id_TipoDocumento').val()==""){
        error = 1;
        
    }
    if($('#id_genero').val()==""){
        error = 1;
        
    }
    if($('#id_fechaNacimiento').val()==""){
        error = 1;
        
    }
    if(error == 1){
        alert("Faltan completar datos");
    }
    else{
        $('#cargarAlumno').submit();
    }
}