# def potencia(numero):
#     potencia = 1


#     while (potencia <= 10):
#         result = numero ** potencia
#         print("potencia de {} elevado a la es {} es {}".format(numero, potencia, result))
#         potencia += 1


# def run():
#     numero = int(input("Escribe el numero el cual quieres averiguarle la portencia"))
#     potencia(numero)


# if __name__=="__main__":
#     run() 


# contador = 0
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 1
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 2
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 3
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 4
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# contador = 5
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador))

# Este codigo repetido se puede resolver con el cilo While (Mientras) de la siguiente forma:


# def run():
#     LIMITE = 1000000

#     contador = 0
#     potencia_2 = 2**contador
#     while potencia_2 < LIMITE:
#         print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
#         contador = contador + 1
#         potencia_2 = 2**contador

# if __name__=="__main__":
#     run()

a = 0

while a<101:
    a = a + 1 #a = a+1
    if a % 2 == 0:
        continue
    print(a)
print("fin")