#16) Hacer un programa para ingresar por teclado las cuatro notas de los exámenes obtenidas
#por un alumno y luego emitir uno solo de los cartel de acuerdo a las siguientes condiciones:
#- “Promociona”, si obtuvo en los cuatro exámenes nota 7 o más.
#- “Rinde examen final”, si obtuvo nota 4 o más en por lo menos tres exámenes.
#- “Recupera Parciales”, si obtuvo nota 4 o más en por lo menos uno de los exámenes.
#- “Recursa la materia”, si no aprobó ningún examen parcial.

def prom(n1,n2,n3,n4):
    if n1>=7 and n2>=7 and n3>=7 and n3>=7:
        return 2
    else:
        return 0

def rinfinal(n1,n2,n3,n4):
    conp=0
    con=0
    for x in [n1,n2,n3,n4]:
        if x>=7:
            conp+=1
        if(x>=4):
            con+=1
    if conp==4:
        return 2
    elif con>=3:
        return 1
    elif con>=1:
        return 0
    elif con==0:
        return -1


n1=int(input("Nota 1:"))
n2=int(input("Nota 2:"))
n3=int(input("Nota 3:"))
n4=int(input("Nota 4:"))
valor=0
valor=rinfinal(n1,n2,n3,n4)
if valor==2:
    print("Promociono")
elif valor==1:
    print("Rinde examen final")
elif valor==0:
    print("Recupera Parciales")
elif valor==-1:
    print("Recursa la materia")
