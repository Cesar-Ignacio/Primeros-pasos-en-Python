
import math

#practicando la recursividad 


def Factoria(n):
    if n==0:
        return 1
    else:
        fac=Factoria(n-1)
        return n* fac

def Fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

#main 


num=int(input("Ingrese numero:"))

print("FACTORIAL DE ", num ,"=", Factoria(num))

num=int(input("Ingrese numero:"))

print("FIBONACCI DE ", num, "=", Fibonacci(num))

