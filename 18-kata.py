def sumatorioNumeros(numero):
    total = 0
    while numero != 0:
        ultimoDigito = numero % 10
        total = total + ultimoDigito
        numero = numero // 10
    return total


n = int(input("Escribe un número:"))
print("Suma de los dígitos:", sumatorioNumeros(n))
