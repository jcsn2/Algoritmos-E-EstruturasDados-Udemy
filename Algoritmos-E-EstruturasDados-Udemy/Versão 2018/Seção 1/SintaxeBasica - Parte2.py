nome = 'Jose Neto'

print(len(nome))

lista = [1,2,3]

print(len(lista))

d = {'marcos': 28, 'Neto': 25}

for chave in d:
    print(d[chave])


num = 10

if(num % 2 == 0):
    print("Número eh par")
else:
    print("Número eh ímpar")

numero = 0

while(numero < 11):
    print(numero)
    numero += 1

def ehPar(num):
    if(num % 2 == 0):
        return True
    return False

print(ehPar(20))