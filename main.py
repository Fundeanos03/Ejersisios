import math

#1
def ex1_1():
    base_rec = float(input("base del rectangulo: "))
    altura_rec = float(input("altura del rectangulo: "))

    area_rec = base_rec * altura_rec
    perimetro_rec = 2 * (base_rec + altura_rec)

    print("area del rectangulo: ", area_rec)
    print("perimetro del rectangulo: ", perimetro_rec)
ex1_1()

#1.2
def ex1_2():
    temperatura = float(input("temperatura en grados Celsius: "))

    F = temperatura * 1.8 + 32
    print("temperatura en Fahrenheit: ", F)
    K = temperatura + 237.15
    print("temperatura en Kelvin: ", K)
    R = temperatura * 0.8
    print("temperatura en Réaumur: ", R)
ex1_2()

#1.3
def ex1_3():
    radio = float(input("Radio de la ésfera: "))
    volumen_esf = 4/3 * math.pi * (radio ** 3)
    print("El volumen de la esfera es ", volumen_esf)
ex1_3()

#1.4
def ex1_4():
    precioZapas = float(input("precio de zapatillas: "))
    descuentoCompra = float(input("descuento de compra: "))
    descuentoAplicado = precioZapas * ((100-descuentoCompra)/100)
    print("El precio de las zapatillas es de :", precioZapas)
    print("El descuento de la compra es de :", descuentoCompra)
    print("El precio final es de: ", descuentoAplicado)
ex1_4()

#1.5
def ex1_5():
    gasolina = float(input("Dinero gasolina: "))
    alojamiento = float(input("Dinero alojamento: "))
    comida = float(input("Dinero comida: "))

    sumaGastos = gasolina + alojamiento + comida
    pGasolina = (gasolina / sumaGastos)*100
    pAlojamiento = (alojamiento / sumaGastos)*100
    pComida = (comida / sumaGastos)*100

    print("La suma total de gastos es de ", sumaGastos)
    print(f"El porcentaje que supone la gasolina es: {pGasolina:.2}")
    print(f"El porcentaje que supone el alojamiento es: {pAlojamiento:.2}")
    print(f"El porcentaje que supone la comida es: {pComida:.2}")

#2.1
def ex2_1():
    numero = int(input("Ingrese un numero entero: "))
    if numero >0:
        print("El numero ingresado es positivo")
    elif numero < 0:
        print("El numero ingresado es negativo")
    else:
        print("El numero ingresado es 0")

#2.2
def ex2_2():
    edad = int(input("Ingrese su edad: "))

    if edad >=16 and edad <=30:
        print("Edad válida para la solicitud")
    else:
        print("Edad no válida para la solicitud")
    if not edad <16 or edad >30:
        print("Edad válida para la solicitud")
    else:
        print("Edad no válida para la solicitud")

#2.3
def ex2_3():


#2.6
def esFechaValida(dia, mes):
    salida = False
    max_dias_mes = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}


    if (1 <=mes <=12) and 1>=dia <= max_dias_mes[mes]:
        salida = True
    return salida

mes = 0
dia = 0

while not esFechaValida(dia, mes):
    dia = int(input("Dime el dia: "))
    mes = int(input("Dime el mes: "))

estacion="invierno"
if((mes in [4,5])) or (mes==3 and dia>=21) or (mes==6 and dia <=21):
    estacion="primavera"
elif ((mes in [7,8])) or (mes==6 and dia>=21) or (mes==9 and dia <=23):
    estacion="verano"
elif ((mes in [10,11])) or (mes==9 and dia>=23) or (mes==12 and dia <=21):
    estacion="otoño"

print(f"El dia {dia} / mes {mes} es: {estacion}")


#3.3

n = int(input("Ingrese un numero entero: "))
suma_total = sum(range(1,n+1)º)