print("Bienvenido a la miscelania de operaciones")
print("seleccione la operación que desea realizar:")
print("operadores    (1)")
print("condicionales (2)")
print("Ciclos        (3)")
print("salir         (99)")
menu_principal = int(input("favor ingrese su selección: "))
while menu_principal != 99:
    if menu_principal == 1:
        print("selecciona una operación")
        print("1.1 Area de un triangulo")
        print("1.2 suma dos numeros")
        print("1.3 numero elevado al cuadrado")
        print("1.4 convertir euros a dolares")
        print("1.5 area y perimetro de un cuadrado")
        print("1.6 area y volumen de un cilindro")
        print("1.7 radio, area y longitud de una circunferencia")
        print("1.8 promedio de tres numeros")
        print("1.9 para salir")
        submenu_oper = float(input("favor seleccione una opción: "))

        if submenu_oper == 1.1:
            base = float(input("ingrese la base [cm]: "))
            altura = float(input("ingrese la altura [cm]: "))
            resultado = base * altura / 2
            print("El area del triangulo es: {} cm".format(round(resultado, 2)))
        elif submenu_oper == 1.2:
            numero1 = int(input("primer numero: "))
            numero2 = int(input("segundo numero: "))
            resultado = numero1 + numero2
            print(resultado)
        elif submenu_oper == 1.3:
            numero1 = int(input("ingrese un numero: "))
            resultado = numero1 ** 2
            print(resultado)
        elif submenu_oper == 1.4:
            dolar = 0.90
            euros = float(input("cuantos euros deseas convertir: "))
            conversion = euros / dolar
            print(float(round(conversion, 2)))
        elif submenu_oper == 1.5:
            lado = float(input("indique la medida de un lado del cuadrado: "))
            perimetro = lado + lado + lado + lado
            area = lado * lado
            print(float(round(perimetro, 2)))
            print(float(round(area, 2)))
        elif submenu_oper == 1.6:
            from math import pi
            perimetro_base = float(input("indique el perimetro de la base del cilindro: "))
            altura_c = float(input("indique la altura del cilindro: "))
            area_lateral = 2 * pi * perimetro_base * altura_c
            area_base = pi * 2.5 ** 2
            area_total = area_lateral + (area_base * 2)
            volumen = area_base * altura_c
            print(f"area base: ", round(area_base, 2))
            print(f"area lateral: ", round(area_lateral, 2))
            print(f"area total: ", round(area_total, 2))
            print(f"volumen: ", round(volumen, 2))
        elif submenu_oper == 1.7:
            contador: int = 0
            suma = 0
            numero = 1
            while numero != 0:
               numero = int(input("Digite un numero entero (0 para terminar): "))
               if numero != 0:
                   suma += numero
                   contador += 1
            if contador == 0:
               print("No digito ningun numero.")
            else:
               promedio = suma / contador
               print("El promedio de los {} números es igual a {}".format(contador, round(promedio, 2)))

    elif menu_principal ==2:
        print("selecciona una operación")
        print("2.1 saber si numero es negativo o positivo")
        print("2.2 saber si un numero es mayor o menor")
        print("2.3 leer tres numeros enteros positivos y saber cual es el mayor y menor")
        print("2.4 Dados dos números A y B, sumarlos si A es menor que B o sino restarlos")
        print("""2.5 Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero
        no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es
        posible""")
        print("""2.6 Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario
        multiplicarlos.""")
        print("2.7 Escribir un algoritmo que determine si un año es bisiesto o no")
        print("2.8 Salir")
        submenu_condicionales = float(input("favor seleccione una opción: "))
        if submenu_condicionales == 2.1:
            numero_pos= (int(input("por favor digite un numero: " )))
            if numero_pos ==0:
                print("el numero es neutro")
            elif numero_pos < 0:
                print("el numero es negativo")
            else:
                print("el numero es positivo")
        elif submenu_condicionales == 2.2:
            n1= (int(input("ingreso el primer numero")))
            n2= (int(input("ingrese el segundo numero ")))
            if  n1 > n2:
                print("el primer numero es mayor")
            else:
                print("el segundo numero es mayor")
        elif submenu_condicionales == 2.3:
            numeros= []
            for i in range(3):
                numero= float(input("introduce el número # {}: ".format(i+1)))
                numeros.append(numero)
            mayor=numeros[0]
            menor=numeros[0]
            for numero in numeros:
                if numero > mayor:
                    mayor=numero
            print("mayor: ",mayor)
            for numero in numeros:
                if numero < menor:
                    menor=numero
            print("menor: ", menor)
        # A y B, si A es mayor sumarlos si no restarlos
        elif submenu_condicionales == 2.4:
            x= int(input("por favor ingrese el primer  numero: "))
            y= int(input("por favor ingrese un segundo numero: "))
            if x > y:
                ans= x + y
                print(f"\n    {x} es mayor que {y} por lo tanto se suma \n \n    Resultado: {ans} \n")
            else:
                ans= x - y
                print(f"\n    {y} es mayor que {x} por lo tanto se resta \n \n    Resultado: {ans} \n")

            # A y B, encontrar cociente entre A y B
        elif submenu_condicionales == 2.5:
            x = int(input("por favor ingrese el primer  numero: "))
            y = int(input("por favor ingrese un segundo numero"))
            if (x==0 and y==0):
                print("\n    ¡No puedes dividir 0 entre 0! \n")
            else:
                ans = x // y
                print(f"\n    El cociente de {x} y {y} es {ans} \n")

                # A y B, encontrar cociente entre A y B
        elif submenu_condicionales == 2.6:
            a = int(input("por favor ingrese el primer  numero: "))
            b = int(input("por favor ingrese un segundo numero: "))
            if (a < 0 and b > 0):
                ans = a + b
                print(f"\n    '{a}' es negativo y se suma \n {a} + {b} = {ans} \n")

            elif (a > 0 and b < 0):
                ans = a + b
                print(f"\n    '{b}' es negativo y se suma \n {a} + {b} = {ans} \n")
            # Comprobador de añor bisiestos
        elif submenu_condicionales == 2.7:
            year = int(input("por favor ingrese el año: "))
            if (year % 4 != 0):
                print( f"\n    {year}, No es Bisisesto! \n")
            elif (year % 4 == 0 and year % 100 != 0):
                print(f"\n    {year} es Bisiesto! \n")
            elif (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
                print(f"\n    {year}, No es Bisiesto! \n")
            elif (year  % 4 == 0 and year % 100 == 0 and year % 400 == 0):
                print(f"\n    {year}, Es Bisiesto! \n")
            else:
                print(f"   no coincide {year}, corrija ??")

    elif menu_principal == 3:
        print("selecciona una operación")
        print("3.1 Imprimir todos los múltiplos de 3 que hay entre 1 y 100.")
        print("3.2 Imprimir los números impares entre 0 y 100.")
        print("3.3 Imprimir los números pares del 1 al 100.")
        print("3.4 Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30")
        print("""3.5 Escribir un programa que sume los cuadrados de los cien primeros números naturales,
        mostrando el resultado en pantalla.""")
        print("""3.6 Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los
        números comprendidos entre ellos en secuencia ascendente..""")
        print("3.7 Sumar todos los números que se digitan por teclado mientras no sea cero.")
        submenu_ciclos = float(input("favor seleccione una opción: "))

        # Imprime los multiplos de 3 entre 1 y 100
        if submenu_ciclos == 3.1:
            def ciclo1(valor, multiple):
             return True if valor % multiple ==0 else False
            multiples_3=[]
            for i in range(1,101):
                if ciclo1 (i,3):
                    multiples_3.append(i)
                print("Los multiplos de 3 son:", multiples_3)

        # Imprimir los números impares entre 0 y 100
        if submenu_ciclos == 3.2:
            x=0
            while x <=100:
                if  x % 2 ==1:
                    print(x)
                x+= 1

        # Imprimir los números pares entre 1 y 100
        if submenu_ciclos == 3.3:
            x = 0
            while x <= 100:
                if x % 2 == 0:
                    print(x)
                x += 1
        if submenu_ciclos == 3.4:
            def generar_cuadrados(n):
                if 2 * n <= 30:
                    cuadrados = [i ** 2 for i in range(1,31)]
                    return cuadrados [:n] + cuadrados[-n:]
                else:
                    raise ValueError("n no debe ser mayor a 2 * n")
            resultado = generar_cuadrados(5)
            print(resultado)
        if submenu_ciclos == 3.5:
            suma=0
            for i in range(100):
                cuadrado = (i+1)*(i+1)
                suma =suma + cuadrado
                print(f"El cuadrado de {i+1}={cuadrado}")
            print(f"La suma es:{suma}")

else:
    print("por favor digite una opción correcta")
    print("operadores    (1)")
    print("condicionales (2)")
    print("Ciclos        (3)")
    print("salir         (99)")
    menu_principal = int(input("favor ingrese su selección: "))






































