# Menu de area
print("   MENU: \n")
print("    1. Operaciones \n    2. Condicionales \n    3. Ciclos \n    0. Salir \n");

opcion = int(input( '--> '))

# Entradas de Modulo Operadores
def operaciones():
    print("---- OPERADORES ----")
    print("\n")
    print("   MENU: \n")
    print(
        "    1. Area de Triangulo \n    2. Sumar dos numeros \n    3. Elevar un numero al cuadrado \n    4. Euros a dolares \n    5. Area y perimetro de un cuadrado \n    6. Area y volumen de un cilindro \n    7. Longitud y area de una circunferencia \n    8. Promedio de tres numeros \n \n    9. Reiniciar \n    0. Salir \n");

    opcion = int(input('--> '))

    if (opcion == 0):
        salirWe()
    elif (opcion == 9):
        reiniciar()
    elif (opcion == 1):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Area de un Triangulo \n")
        base = int(input(Fore.RESET + "    Base del triangulo en cm: "))
        altura = int(input("    Altura del triangulo en cm: "))
        print(Fore.YELLOW + "\n    El area del triangulo es:", operadores.areaTri(base, altura), "\n")

    elif (opcion == 2):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Suma dos numeros \n")
        num1 = int(input(Fore.RESET + "    Ingresa el primer valor: "))
        num2 = int(input("    Ingresa el segundo valor: "))
        print(Fore.YELLOW + "\n    El resultado es:", operadores.suma(num1, num2), "\n")

    elif (opcion == 3):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Eleva un numero al cuadrado \n")
        num = int(input(Fore.RESET + "    Ingresa el valor: "))
        print(Fore.YELLOW + f"\n    {num} elevado, es {operadores.elevar(num)} \n")

    elif (opcion == 4):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Convertidor Euros a Dolares \n  ( 0.90 EUR --> 1 USD ) \n")
        num = int(input(Fore.RESET + "    Cuantos Euros tienes?: "))
        print(Fore.YELLOW + f"\n    {num} EUR son {operadores.convertidor(num)} USD \n")

    elif (opcion == 5):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Calcula el Area y Perimetro \n  de un cuadrado \n")
        num = int(input(Fore.RESET + "    Cuanto miden los lados?(cm): "))
        print(
            Fore.YELLOW + f"\n    Lados de: {num} cm \n    Area: {operadores.area(num)} cm² \n    Perimetro: {operadores.perimetro(num)} cm \n")

    elif (opcion == 6):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Calcula el Area y Volumen \n  de un cilindro \n")
        base = float(input(Fore.RESET + "    Escribe el diametro de la base del cilindro?(cm): "))
        altura = float(input("    Cual es la altura del cilindro?(cm): "))
        areaCil = operadores.areaCil(base, altura)
        volCil = operadores.volCil(base, altura)

        print(Fore.YELLOW + f"\n    Area Total: {round(areaCil, 2)} cm² \n    Volumen Total: {round(volCil, 2)} cm² \n")

    elif (opcion == 7):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Calcula la longitud y area \n  de una circunferencia \n")
        num = int(input(Fore.RESET + "    Cuanto mide el radio?(cm): "))
        print(
            Fore.YELLOW + f"\n    Radio: {num} cm \n    Longitud: {num * 2} cm \n    Area: {operadores.areaCir(num)} cm² \n")

    elif (opcion == 8):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Calcula el promedio de tres numeros \n")
        num1 = float(input(Fore.RESET + "    Dame el primer numero: "))
        num2 = float(input(Fore.RESET + "    Dame el segundo numero: "))
        num3 = float(input(Fore.RESET + "    Dame el tercer numero: "))
        ans = operadores.promedio(num1, num2, num3)

        print(
            Fore.YELLOW + f"\n    El promedio de {round(num1, 2)}, {round(num2, 2)}, {round(num3, 2)} --> {round(ans, 2)} \n")


# Entradas de Modulo Condicionales
def condiciones():
    print(Fore.CYAN + "-----" * 10)
    print(Fore.BLUE + "             ---- CONDICIONALES ----")
    print(Fore.CYAN + "-----" * 10, "\n")
    print(Fore.RESET + "   MENU: \n")
    print(
        "    1. Tu numero es positivo o negativo? \n    2. Calcular cual numero es mayor \n    3. Cual de los numero es mayor y menor \n    4. A es menor que B o sino restarlos \n    5. Cociente de dos numeros \n    6. Dos numeros, segun su valor sumar o multiplicar \n    7. Determinar si un año es bisiesto o no \n \n    8. Reiniciar \n    0. Salir \n");

    opcion = int(input(Fore.GREEN + '--> '))

    if (opcion == 0):
        salirWe()
    elif (opcion == 8):
        reiniciar()
    elif (opcion == 1):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  ¿Numero positivo o negativo? \n")
        num = int(input(Fore.RESET + "    Ingresa un numero: "))

        condicionales.posiNega(num)
    elif (opcion == 2):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Calcula cual numero es mayor y menor \n")
        num1 = int(input(Fore.RESET + "    Ingresa el primer numero: "))
        num2 = int(input(Fore.RESET + "    Ingresa el segundo numero: "))

        condicionales.calMenMay(num1, num2)
    elif (opcion == 3):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Cual de los numeros es mayor y menor \n")
        num1 = int(input(Fore.RESET + "    Ingresa el primer numero: "))
        num2 = int(input(Fore.RESET + "    Ingresa el segundo numero: "))
        num3 = int(input(Fore.RESET + "    Ingresa el tercero numero: "))

        condicionales.calTresNum(num1, num2, num3)
    elif (opcion == 4):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  A es menor que B sumar si no restar \n")
        num1 = int(input(Fore.RESET + "    Ingresa el primer numero: "))
        num2 = int(input(Fore.RESET + "    Ingresa el segundo numero: "))

        weon = None
        condicionales.abSumRest(num1, num2)
    elif (opcion == 5):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Cociente de dos numeros A y B \n")
        num1 = int(input(Fore.RESET + "    Ingresa el primer numero: "))
        num2 = int(input(Fore.RESET + "    Ingresa el segundo numero: "))

        condicionales.abCosciente(num1, num2)
    elif (opcion == 6):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Dos numeros segun su valor sumar o restar \n")
        num1 = int(input(Fore.RESET + "    Ingresa el primer numero: "))
        num2 = int(input(Fore.RESET + "    Ingresa el segundo numero: "))

        condicionales.abSumMul(num1, num2)
    elif (opcion == 7):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Calcula que si el año es Bisiesto \n")
        numY = int(input(Fore.RESET + "    Ingresa el año: "))

        condicionales.añoBisiesto(numY)


# Entradas de Modulo Ciclos
def ciclones():
    print(Fore.CYAN + "-----" * 10)
    print(Fore.BLUE + "             ---- CONDICIONALES ----")
    print(Fore.CYAN + "-----" * 10, "\n")
    print(Fore.RESET + "   MENU: \n")
    print(
        "    1. Multiplos de 3 que hay entre 1 y 100 \n    2. Numeros impares entre 0 y 100 \n    3. Numeros pares del 1 al 100 \n    4. Cuadrados de los numeros del 1 al 30 \n    5. Suma de cuadrados de los primeros cien numeros naturales \n    6. Dos numeros comprendidos entre ellos en secuencia ascendente \n    7. Suma todos los numeros que se digitan por teclado mientras no sea cierto \n \n    8. Reiniciar \n    0. Salir \n");

    opcion = int(input(Fore.GREEN + '--> '))

    if (opcion == 0):
        salirWe()
    elif (opcion == 8):
        reiniciar()
    elif (opcion == 1):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Multiplos de 3 entre 1 y 100 \n")

        ciclos.ciclo_1()
    elif (opcion == 2):
        print(Fore.CYAN + "-----" * 10)
        print(Fore.BLUE + "  Numeros impares del 0 al 100 \n")

        ciclos.numImpares()


# Menu de inicio
def inicio():
    if (opcion == 0):
        salirWe()
    elif (opcion == 1):
        operaciones()
    elif (opcion == 2):
        condiciones()
    elif (opcion == 3):
        ciclones()
    else:
        print(Fore.RED + " ¡Escoge un numero valido!")
        exit()


# Flujo
inicio()

# Entradas de Modulo Condicionales

# Entradas de Modulo Ciclos

