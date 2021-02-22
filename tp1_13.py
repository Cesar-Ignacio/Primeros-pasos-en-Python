#13) Hacer un programa para un cajero automático para ingresar un importe a retirar y convertir
#el mismo en la cantidad de billetes de $ 1.000, $ 500, $ 200 y $ 100 a entregar.
#Ejemplo 1: Si el importe a retirar es $ 2.500 se mostrara por pantalla que se deberán entregar 2
#billetes de $ 1.000, 1 billete de $ 500 y 0 billetes de $ 200 y $ 100. SIGUE 
#- 4 -
#Ejemplo 2: Si el importe a retirar es $ 3.400 se mostrara por pantalla que se deberán entregar 3
#billetes de $ 1.000, 2 billetes de $ 200 y 0 billetes de $ 500 y $ 100.
#Ejemplo 3: Si el importe a retirar es $ 300 se mostrara por pantalla que se deberán entregar 1
#billete de $ 200, 1 billete de $ 100, 0 billetes de $ 1.000 y 0 billetes de $ 500.
#Recordatorio. Considerar en todos los casos que el importe a retirar es en todos los casos
#múltiplo de $ 100 ya que el cajero no cuenta con billetes de $ 50, $ 20 o $ 10.

#funciones

    
def mostrar(dinero):
    mil=int(dinero/1000)
    resto=int(dinero%1000)
    quinientos=int(resto/500)
    resto=int(resto%500)
    docientos=int(resto/200)
    resto=int(resto%200)
    cientos=int(resto/100)
    resto=int(resto%100)
    return mil,quinientos,docientos,cientos
        


#main

importe=int(input("Ingrese importe:"))

v=mostrar(importe)
mi=0
quinientos=0
docientos=0
cientos=0
c=0
for x in v:
    c+=1
    if c==1:
        mi=x
    if c==2:
        quinientos=x
    if c==3:
        docientos=x
    if c==4:
        cientos=x
    
print("Billetes de mil:",mi)
print("Billetes de quinientos:",quinientos)
print("Billetes de docientos:",docientos)
print("Billetes de cienes:",cientos)
