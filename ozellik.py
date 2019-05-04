def ekok(sayi1, sayi2):
    i = 2
    ekok = 1

    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            sayi1 /= i
            sayi2 /= i
            ekok *= i

        elif (sayi1 % i == 0 and sayi2 % i != 0):
            sayi1 /= i
            ekok *= i

        elif (sayi1 % i != 0 and sayi2 % i == 0):
            sayi2 /= i
            ekok *= i
        else:
            i +=1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok

print(ekok(5,6))