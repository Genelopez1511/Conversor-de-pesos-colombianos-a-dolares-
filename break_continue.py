def run():
    # for contador in range(1000):
    #     if contador % 2 != 0: # si contador divido entre 2, da residuo saltar si da residuo 0 ingresarlo
    #         continue
    #     print(contador)

    # for i in range(1000):
    #     print(i)
    #     if i == 500: # si i vale 500 parar el ciclo
    #         break

    texto = input("escribe algo: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    run()

