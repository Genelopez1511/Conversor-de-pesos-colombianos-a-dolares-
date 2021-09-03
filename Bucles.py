def potencia(numero):
    potencia = 1


    while (potencia <= 10):
        result = numero ** potencia
        print("potencia de {} elevado a la es {} es {}".format(numero, potencia, result))
        potencia += 1


def run():
    numero = int(input("Escribe el numero el cual quieres averiguarle la portencia"))
    potencia(numero)


if __name__=="__main__":
    run() 