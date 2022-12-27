function borrar (url,id){
    opcion=confirm(`¿Está seguro que desea eliminar?`);
    if (opcion==true){
        window.location.href=url + id
    }
}

function borrarAlumnoCoorte (id, idCoorte){
    opcion=confirm(`¿Está seguro que desea eliminar?`);
    if (opcion==true){
        window.location.href= '../eliminarAlumnoCoorte/'+id+'/'+idCoorte+''
    }
}
