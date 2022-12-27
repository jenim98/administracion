function borrar (nombre,url,id){
    alert(id)
    opcion=confirm('¿Está seguro que desea eliminar' +nombre+'?');
    if (opcion==true){
        window.location.href=url + id
    }
}
