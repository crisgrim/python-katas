def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print('Booom!')
    print('Function end', str(numero))


cuenta_regresiva(10)