# ---------------------------------------------------------------------------
# Autor: Dirk Tiede - UNIGIS - tes1
# Fecha: 10/01/2017
# Contacto: Antonio Pantoja @PantojaAntonio apantoja.ciat@gmail.com
# convertir coordenadas de escritura decimal, a grados, minutos, segundos

import string
def convDec(inCoor):
    value1 = string.split(inCoor, ".")
    deg = int(value1[0])
    if deg > 0:
        pre = "N"
    elif deg < 0:
        pre = "S"
        deg = -deg
        inCoor = -float(inCoor)
    x = 60*(float(inCoor)-deg)
    value2 = string.split(str(x), ".")
    min = int(float(value2[0]))
    sec = int((x-min)*60)
    return pre + str(deg) + " Grad " + str(min)+ " Min " + str(sec) + " Seg "
# Entrada de las coordenadas
decCoor = raw_input ("Por favor inserte una coordenada de latitud en escritura decimal: ")
# llamada de la funcion con transmision de variable
latlong = convDec (decCoor)
# salida del valor emitido por la funcion
print "La coordenada en Grados, Minutos, Segundos es: " + latlong