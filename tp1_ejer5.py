#5) Un comercio vende tres marcas de alfajores distintas A, B y C.
#Hacer un programa para ingresar por teclado la cantidad de alfajores vendidos de cada una de
#las tres marcas y luego se informe el porcentaje de ventas para cada una de ellas.
#Ejemplo. Si se ingresa 100, 25 y 75 como cantidades vendidas entonces el programa calculará
#e informará A: 50%, B: 12,50% y C: 37,50%.

def  Porcentaje(C,total):
    C= float(C*100)/total
    
    return C


A=int (input("INGRESA CANTIDA DE ALFAJOR A:"))
B=int (input("INGRESA CANTIDA DE ALFAJOR B:"))
C=int (input("INGRESA CANTIDA DE ALFAJOR C:"))

tataventa=A+B+C

#FA= float(A*100)/tataventa
#FB= float(B*100)/tataventa
#FC= float(C*100)/tataventa


print("PORCENTAJE DE VENTA DE ALFAJOR A:",Porcentaje(A,tataventa))
print("PORCENTAJE DE VENTA DE ALFAJOR B:",Porcentaje(B,tataventa))
print("PORCENTAJE DE VENTA DE ALFAJOR C:",Porcentaje(C,tataventa))

print("CANTIDAD DE ALFAJORES VENDIDOS:",tataventa)