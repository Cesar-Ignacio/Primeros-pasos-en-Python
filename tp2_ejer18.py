#18) Una empresa de electricidad cobra el servicio a sus clientes de acuerdo a la siguiente 
#escala:
#$ 10 por kilovatio por el consumo hasta los primeros 100 kilovatios de consumo.
#$ 12 por kilovatio por el consumo excedente de 101 a 200 kilovatios.
#$ 15 por kilovatio por el consumo excedente de 201 kilovatios en adelante.
#Hacer un programa para que, dado el consumo en kilovatios de un determinado cliente, el 
#programa calcule e informe el total a pagar por el mismo.
#Ejemplo 1: Un consumo de 55 kilovatios, se calculará: $ 10 x 55= $ 550
#Ejemplo 2: Un consumo de 125 kilovatios, se calculará: $ 10 x 100 + $ 12 x 25=$ 1300
#Ejemplo 3: Un consumo de 250 kilovatios, se calculará: $ 10 x 100 + $ 12 x 100 + $ 15 x 50 = $ 2950


def importe(consumo):

    importe=0

    if consumo<=100:
        importe=consumo*10
    elif consumo>100:
        importe=100*10
        consumo=consumo-100
       
        if consumo>0 and consumo<=100:
            
            importe+=consumo*12
            
        elif consumo>100:
            importe+=100*12
            consumo=consumo-100
            importe+=consumo*15
            
    return importe




#main

y=0

while y<3:
    consumo=int(input("Ingrese consumo:"))
    print("TOTAL A PAGAR:",importe(consumo))
    y=y+1

