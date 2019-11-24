entrada = ""
suma = 0
while suma < 3 and entrada != "despedida":
    entrada = input("Clave: ")
    suma += 1
    print("Intento %d. \n " % suma)
print("Utilizaste %d intentos." % suma)
#fin_interador
print("Fin de bucle")
