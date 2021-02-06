#6) Hacer un programa para que un comercio ingrese por teclado la recaudación en pesos para
#cada una de las cuatros semanas del mes. El programa debe listar la recaudación promedio por
#semana y el porcentaje de recaudación por semana.
#Ejemplo. Si se ingresa $ 1600, $ 1200, $ 4800 y $ 400 se listara como recaudación promedio
#$ 2000 y como porcentajes por semana: 20%, 15%, 60% y 5%.

import time as tm

def Porcen(c,t):
  por=(c*100)/t
  return por

sp=float(input("Primera semana:"))
ss=float(input("Segunda semana:"))
st=float(input("Tercera semana:"))
sc=float(input("Cuarta semana:"))

prom= float((sp+ss+st+sc)/4)
t=float(sp+ss+st+sc)
print ("PROMEDIO:",prom)

print("Porcetaje p_semana",Porcen(sp,t))
print("Porcetaje s_semana",Porcen(ss,t))
print("Porcetaje t_semana",Porcen(st,t))
print("Porcetaje c_semana",Porcen(sc,t))

tm.sleep(10)

print("CHAUUU")