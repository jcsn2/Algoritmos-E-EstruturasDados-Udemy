lista = [1,2,3]
tupla = (1,2,3)

a,b,c = lista
d,e,f = tupla

print(a,b,c)
print(d,e,f)

#Ignorando elementos
listaNova = [1,2,3,4]

z1, z2 , _, _ = listaNova

print(z1,z2)

#String
nome = 'abc'

c1, c2, c3 = nome

print(c1,c2,c3)

def func(x,y):
    return x ** 2, y ** 2

r1, r2 = func(2,3)

print(r1, r2)

#Parametro Opcional
def func(x,y = 3):
    #Se não for passado valor de y ele considerará 3
    pass

