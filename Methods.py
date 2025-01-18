from calendar import c
from pickle import TRUE
from sympy import *
import numpy 
from prettytable import PrettyTable
mytable = PrettyTable(["Метод", "a,b,x0", "Значение корня xn", "кол-шагов"])
count = 0
x=symbols('x')
a=diff(x**3-5*x+1,x,2)


def func(z):#сама функция
    x=z
    return x**3-5*x+1
def derivative_1(z):#перавя производная функции
    der=diff(x**3-5*x+1)
    f1=lambdify(x,der)
    return f1(z)
def derivative_2(z):#вторая производная функции
    der=diff(x**3-5*x+1,x,2)
    f1=lambdify(x,der)
    return f1(z)

def Dehotomiy (a,b,eps):#метод половинного деления
    global count
    count = 0
    while TRUE:
        e=(a+b)/2
        if func(e)*func(b)<0:
            a=e
        else:
            b=e
        count=count+1
        if(b - a < eps):
            break
    return e 
def hord(a,b,eps):#метод хорд
    global count
    count = 0
    if func(a)* derivative_2(a) > 0 :
        xn = a
        while TRUE:
            x0=xn
            xn= xn-func(xn)*(b-xn)/(func(b)-func(xn))
            count=count+1
            if(abs(x0-xn) <= eps):
                break
    else :

        xn = b
        while True:
            x0=xn
            xn= a-func(a)*(xn-a)/(func(xn)-func(a))
            print(xn)
            count=count+1
            if(abs(x0-xn) <= eps):
                break
    
    return xn
def kasat (a,b,eps): #метод Ньютона
    global count
    count = 0
    if func(a)*derivative_2(a)>0:
        xn = a     
    else:
        xn=b
    while True:
        x0=xn
        xn = xn-func(xn)/derivative_1(xn)
        count=count+1
        if(abs(x0-xn) <= eps):
                break
    return(xn)
def comb(a,b,eps): # комбинированный метод
    global count
    count = 0
    if func(a)*derivative_2(a)>0:
        xn = a
        xnn =b
        while   True:
            xn = xn-func(xn)/derivative_1(xn)
            xnn = xn-func(xn)*(xnn-xn)/(func(xnn)-func(xn))
            count=count+1
            if(abs(xnn-xn) <= eps):
                break
    else:
        xn=b
        xnn=a
        while True:
            xn = xn-func(xn)*(xnn-xn)/(func(xnn)-func(xn))
            xnn = xnn-func(xnn)/derivative_1(xnn)
            count=count+1
            if(abs(xnn-xn) <= eps):
                break
    return(xn)

def iter(a,b,eps): #метод итераций
    global count
    count = 0
    xn=b
    while True:
        x0=xn
        xn= -0.1*xn*xn*xn+0.3*xn*xn-0.2*xn+0.9
        count=count+1
        if (abs(xn-x0)<=eps):
            break
    return(xn)
    



if __name__ == "__main__": 
    a=0
    b=1
    e=0.000001
    mytable.add_row(["Метод дехотомии","[0:1];0",round(Dehotomiy(a,b,e),6),count])
    mytable.add_row(["Метод хорд","[0:1];0",round(hord(a,b,e),6),count])
    mytable.add_row(["Метод касательных","[0:1];0",round(kasat(a,b,e),6),count])
    mytable.add_row(["Метод комбинированный","[0:1];--",round(comb(a,b,e),6),count])
    mytable.add_row(["Метод итерации","[0:1];1",round(iter(a,b,e),6),count])
    print (mytable)
