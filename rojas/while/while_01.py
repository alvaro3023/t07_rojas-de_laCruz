#mostrar el volumen
volumen = float(input("Ingrese volumen: "))
print(volumen)
volumen_incorrecto = (volumen < 40.3 or volumen > 98.4)

#validad que volumen esta entre los rangos de 40.3 y 98.4
while(volumen_incorrecto==True):
    volumen= float(input("Ingrese volumen: "))
    volumen_incorrecto=(volumen < 40.3 or volumen > 98.4)

#fin_while
print("FIN DE BUCLE")
