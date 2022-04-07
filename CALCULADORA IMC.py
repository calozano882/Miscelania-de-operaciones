# calcular tu IMC
print("buenos dias hoy calcularemos tu masa corporal")
peso= float(input("por favor ingresa tu peso: "))
estatura= float(input("por favor ingresa tu estatura: "))
imc= peso/estatura**2
if imc < 18.5:
    print("peso bajo")
elif 18.5 <= imc and imc <25:
    print("peso normal")
elif 25 <= imc and imc < 30:
    print("Sobrepeso")
else:
    print("obesidad")

print ("IMC",round(imc,2))







