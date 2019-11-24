#mostrar el area
area = float(input(("El area es: ")))
print(area)
area_invalida=(area <10 or area>50)
#validar del area este entre 0 y 50
while(area_invalida == True):
    area =float(input(("El area es: ", area)))
    area_invalida=(area <10 or area>50)
#fin_while
print("Fin de bucle")

