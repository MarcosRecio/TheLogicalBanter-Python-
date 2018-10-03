#Sum of the Even Fibonacci Numbers
fibonacci=[]
x=0
y=1
num = int(input("Numero de elementos:"))
for n in range(num):
    aux = x + y
    if aux>=4000000:
        break
    if aux%2==0:
        fibonacci.append(aux)
    x = y
    y = aux
    
print(fibonacci)

suma=0
for i in fibonacci:
    suma=suma+i
print(suma)
