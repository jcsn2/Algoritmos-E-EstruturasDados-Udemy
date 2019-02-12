from collections import deque

d = deque()
d.append(1) # adiciona do lado direito (Segundo, Final)
d.appendleft(2) # adiciona do lado esquerdo (Primeiro, Inicio)
d.append(3)
d.appendleft(4)

# 4, 2, 1, 3

#pop remove do lado direito
#popleft remove do lado esquerdo

d.remove(2) #remove o elemento

for i in d:
	print(i, end=' ')

'''
Deck já está implementado no Python
'''