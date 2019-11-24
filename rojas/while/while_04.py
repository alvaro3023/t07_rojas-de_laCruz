#mostrar el peso
peso = float(input("Ingrese peso: "))
print(peso)
peso_inexacto = (peso < 50.6 or peso > 100.7)
#validad que peso esta entre los rangos de 50.6 y 100.7
while(peso_inexacto==True):
    peso= float(input("Ingrese peso: "))
    peso_inexacto=(peso < 50.6 or peso > 100.7)
#fin_while
print("FIN DE BUCLE")



