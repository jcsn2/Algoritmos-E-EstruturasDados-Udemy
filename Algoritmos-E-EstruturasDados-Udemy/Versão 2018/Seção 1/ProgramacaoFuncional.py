def fat(n):
    if(n == 0):
        return 1
    return (n * fat(n - 1))

print(fat(3))

fat_ = lambda n: n * fat(n - 1) if n > 1 else 1

print(fat_(5))

#map (aplicar uma função pra mais de uma sequencia)

lista = [1,2,3]
m = map(lambda x: x ** 2, lista)

for i in m:
    print(i)

#reduce (aplica uma funcao sobre uma sequencia e vai acumulando o valor de retorno da funcao, a partir de um valor inicial)

import functools

print(functools.reduce(lambda x,y: x+y, [1,2,3,4]))

#Filter(filtra elementos correspondentes a um predicado)

f = filter(lambda x: x % 2 == 0, range(10))

for i in f:
    print(i)