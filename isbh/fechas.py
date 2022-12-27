from datetime import datetime
def fechaAFlotante(fecha):
    fechaDev=float(str(fecha.year)+'.'+str(fecha.month)+str(fecha.day))
    return fechaDev

def calcularEdad(fechaNacimiento):
    fechaM=fechaAFlotante(fechaNacimiento)
    fechaH=fechaAFlotante(datetime.today())
    print(fechaM)
    print(fechaH)
    resultado=fechaH-fechaM
    return resultado

def calcularEdad2(fechaNacimiento):
    fechaH=datetime.today()
    print((fechaH-fechaNacimiento)/365.245)
    ano=int(fechaH.year)-int(fechaNacimiento.year)
    mes=int(fechaH.month)-int(fechaNacimiento.month)
    dia=int(fechaH.day)-int(fechaNacimiento.day)
    if mes<0:
        ano=ano-1
    elif mes==0:
        if dia<0:
            ano=ano-1

def averiguarFecha(xano):
    hoy=datetime.today()
    resu=int(hoy.year)-int(xano)
    fecha=str(resu)+'/'+str(hoy.month)+'/'+str(hoy.day)
    resultado=fecha=datetime.strptime(fecha,'%Y/%m/%d')
    return resultado
   





