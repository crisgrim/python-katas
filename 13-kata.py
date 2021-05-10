def separar(numbers):
    numbers.sort()
    pares = []
    impares = []
    for number in numbers:
        if number % 2:
            pares.append(number)
        else:
            impares.append(number)
    return pares, impares

pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
