#mostrar un si es una estacion del año
estacion=""
estacion_invalido=True

while (estacion_invalido):
    estacion=input("ingrese estacion del año:")
    estacion_invalido=(estacion!="primavera" and estacion!="verano" and estacion!="invierno" and estacion!="otoño")

#fin_while
print("Fin del bucle")
