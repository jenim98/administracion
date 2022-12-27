var traer=0;
function traerLocalidad(t){
    retorno=window.open("../traerlocalidad/", "ventana1", "toolbar = no, top = 500, left = 500, scrollbars = yes");
    traer=t;
}
function enviarLocalidad(id, nombre){
    window.opener.setValue(id, nombre);
    closeOpenerWindow();
}
function setValue(id, nombre) {
    if(traer === 1){
        $('#id_nombreLN').val(id);
        $('#id_localidadNacimiento').val(nombre);
    } else{
        $('#id_nombreLR').val(id);
        $('#id_localidadResidencia').val(nombre);
    }
    retorno.close()
}