# Primer paso se solicita al cliente ingresar cantidad de pesos
pesos = input("Cuantos pesos colombianos tienes?: ")
# en la variable pesos se la coloca tipo float (con decimales)
pesos = float(pesos)
# en esta variable se coloca el valor del dolar en pesos
valor_dolar = 3875
# La cantidad de dolares sera igual a pesos /valor dolar
dolares = pesos / valor_dolar
# Para que nos nos salga una cantidad excesiva de decimales se coloca tipo round la variable que aplica y cuantos decimales
dolares = round(dolares, 2)
# se lleva como string
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
