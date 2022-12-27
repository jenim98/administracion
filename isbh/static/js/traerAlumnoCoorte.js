var traer=0;
function traerAlumno(t){
    retorno=window.open("../agregarAlumnoCoorte/", "ventana1", "toolbar = no, top = 500, left = 700, scrollbars = yes");
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
                        '<td hidden><input type="number" value="'+data[0]['id']+'"></td>',
                        '<td>'+data[0]['Apellido']+', '+data[0]['Nombres']+'</td>',
                        '<td>'+data[0]['Genero_id__descripcion']+'</td>',
                        '<td>'+data[0]['LocalidadVive_id__nombre']+'</td>',
                        '<td>'+data[0]['Telefono']+'</td>',
                        '<td>'+data[0]['Email']+'</td>',
                        '<td><a onclick="eliminarAlumno('+data[0]['id']+')"><i style="color: #000000; cursor:pointer;" class="fa-solid fa-trash-can"></i></a></td>',
                    '</tr>'
                ].join();
                html = html + agregar 
               $('#tablaAlumnosAgregados').append(html);
            }
        });
    
    
    retorno.close();
}
function eliminarAlumno(id){
    opcion=confirm("¿Está seguro que desea eliminar?");
    if (opcion==true){
        $("#tr"+id).remove();
    }
}
function guardarLista(){
    i = 0;
    $('#tablaAlumnosAgregados tr').each(function(index) {
        $(this).find(":input").prop('name','registro'+i);
        i = i + 1;
    })
    $('#cantidadAlumnosNuevos').val(i);
    $('#cargarAlumnosNuevos').submit();
};