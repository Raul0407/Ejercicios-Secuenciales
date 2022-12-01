#EJERCICIO 20

Vnum=[]
num_pri=0
i=2
numerodeprim=int(input("Dime el número de números primos que quieres imprimir por pantalla:\n"))
contador=numerodeprim

def numero_primo(numero):
    num_primo=0
    for i in range (2,numero):
        if numero%i==0:
            num_primo+=1
    if num_primo>=1:
        return False
    else:
        return True
    

while contador>0:
    if numero_primo(i)==True:
        Vnum.append(i)
        contador-=1
    i+=1
print(Vnum)