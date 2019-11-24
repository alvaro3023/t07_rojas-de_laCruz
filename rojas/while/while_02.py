#mostrar un si es un dia de la semana
dia=""
dia_incorrecto=True

while (dia_incorrecto):
    dia=input("ingrese dia:")
    dia_incorrecto=(dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="jueves" and dia!="viernes" and dia!="sabado" and dia!="domingo")

#fin_while
print("Fin del bucle")
