menu = """
Bienvenido al conversor de monedas 💲

1- Pesos colombianos
2- Pesos argentinos
3- Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

def conversion():
    pesos = float(input("Cuantos pesos tienes?: "))
    dolares = round ((pesos / trm),2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

if opcion == 1:
    trm = 3.834
    conversion()
elif opcion == 2:
    trm = 97.48
    conversion()
elif opcion == 3:
    trm = 20.20
    conversion()
else:
    print("Ingresa una opcion correcta")