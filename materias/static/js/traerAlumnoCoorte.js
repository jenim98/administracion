var traer=0;
function traerAlumno(t){
    retorno=window.open("../agregarAlumnoCoorte/", "ventana1", "toolbar = no, top = 500, left = 500, scrollbars = yes");
    traer=t;
}
function enviarAlumno(id){
    window.opener.setValue(id);
    closeOpenerWindow();
}
function setValue(id) {
    $.ajax(
            {type: 'GET',
            url: "../cargarAlumno/",
            data: {id:id},
            success: function(data){
                var html="";
                agregar = [
                    '<tr id="tr'+id+'">',
                        '<td hidden>'+data[0]['id']+'</td>',
                        '<td>'+data[0]['Apellido'],data[0]['Nombres']+'</td>',
                        '<td>'+data[0]['Genero_id__descripcion']+'</td>',
                        '<td>'+data[0]['LocalidadVive_id__nombre']+'</td>',
                        '<td>'+data[0]['Telefono']+'</td>',
                        '<td>'+data[0]['Email']+'</td>',
                        '<td><a onclick="eliminarAlumno('+data[0]['id']+')"><i style="color: #000000; cursor:pointer;" class="fa-solid fa-trash-can"></i></a></td>',
                    '</tr>'
                ].join();
                html = html + agregar 
               $('#tablaAlumnos').append(html);
            }
        });
    
    
    retorno.close();
}
function eliminarAlumno(nombre, id){
    opcion=confirm("¿Está seguro que desea eliminar " + nombre + "?");
    if (opcion==true){
        $("#tr"+id).remove();
    }
}
function guardarLista(){
    $('#cargarAlumno').submit();
};