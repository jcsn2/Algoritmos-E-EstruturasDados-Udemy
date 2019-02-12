import random

#Valores entre 0 e 9
print(random.randrange(10))

#Valores com intervalo entre 1 e 4
print(random.randint(1,4))

lista = [1,2,3,4]

#Escolher um elemento aleatorio
print(random.choice(lista))

#Escolher um elemento com lista embaralhada
random.shuffle(lista)
print(lista)

#Escolher k elementos da lista
print(random.sample(lista,2))

#Gerar numero de ponto fluante entre um valor e outro
print(random.uniform(1,10))