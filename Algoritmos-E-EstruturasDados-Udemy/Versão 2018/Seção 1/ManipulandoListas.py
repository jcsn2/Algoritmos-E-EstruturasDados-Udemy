#Concatenação de Listas
lista1 = [1,2,3,4]
lista2 = [5,6,7,8,9,10]

lista3 = lista1 + lista2

print(lista3)

#Remoção de elementos de listas pelo índice
lista = [1,2,3,4]

lista.pop(0)

print(lista)

#Remoção de elementos de listas por elemento
lista5 = [1,2,3,4]

lista5.remove(2)

print(lista5)

#Busca dos Elementos
lista = [1,2,3,4]

num = 4

if num in lista:
    print("Elemento Encontrado")
else:
    print("Elemento não encontrado")

#Inserir Elementos

listaNova = [1,2,3,4]

listaNova.insert(1,10)

listaNova.sort()

print(listaNova)

