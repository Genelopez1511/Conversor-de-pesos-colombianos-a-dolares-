def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round ((pesos / valor_dolar),2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💲

1- Pesos colombianos
2- Pesos argentinos
3- Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)    
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta")