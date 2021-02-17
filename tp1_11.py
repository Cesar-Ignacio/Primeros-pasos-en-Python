#11) Hacer un programa para ingresar por teclado una cantidad de cantidad de minutos y
#mostrar por pantalla a cuantos días, horas y minutos equivalen.
#Ejemplo 1: si se ingresan 1520 minutos el programa mostrará por pantalla que equivalen a 1
#día, 1 hora y 25 horas.
#Ejemplo 2: si se ingresan 480 minutos el programa mostrará por pantalla que equivalen a 0
#día, 8 horas y 0 minutos.


def MinutosAhoras(minu):
    global resto
    hora=minu/60
    resto=minu%60
    return hora




minutos=int (input("Ingrese minutos:"))

if minutos<60:
    print("Minutos:",minutos)

elif minutos>=60:

    j=MinutosAhoras(minutos)
    #if j>=24:
    print("Dias:",int(j/24))
    print("Horas:",int(j%24))
    print("Minutos:",resto)






