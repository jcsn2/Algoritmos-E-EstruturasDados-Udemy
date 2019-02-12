lista = [1,2,3]

for i in range(len(lista)):
    print(lista[i])

for i in range(1, 10, 2):
    print(i)

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obterNome(self):
        return self.nome

    def obterIdade(self):
        return self.idade

p = Pessoa('José Neto', 25)
print('Nome: {} | Idade: {}'.format(p.obterNome(), p.obterIdade()))

p1 = Pessoa("João" , 28)
p2 = Pessoa("Marcos" , 22)
p3 = Pessoa("Ricardo" , 40)

pessoas = []

pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)

for x in pessoas:
    print(x.obterNome())

pares = [num for num in range(101) if (num % 2 == 0)]
print(pares)