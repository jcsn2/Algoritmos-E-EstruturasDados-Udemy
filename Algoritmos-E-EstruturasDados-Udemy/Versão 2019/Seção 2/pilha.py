'''
FILO(First in, Last out)
Pilha é uma estrutura de dados, forma de armazenar informação
Ela permite inserir e remover elementos
A pilha vai crescendo sempre para cima, o elemento seguinte é sempre inserido no topo.
O elemento e sempre inserido ao final da pilha, o primeiro inserido será o primeiro a ser a chamado.
Na hora de remover, o elemento a ser removido primeiro é o ultimo inserido. Sempre se remove do topo da pilha.
Pilha também pode ser chamada de Stack.
Método append sempre insere ao final.
'''

class Stack:

    def __init__(self):
        self.stack = []

    # Inserir na Pilha
    def push(self, e):
        self.stack.append(e)

    #Remover da Pilha
    def pop(self):
        if not self.empty(): #Se a lista não estiver vazia
            self.stack.pop(len(self.stack) - 1)

    # Saber o elemento do Topo(Último Elemento)
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    # Verificar se a pilha eh vazia
    def empty(self):
        if(len(self.stack) == 0):
            return True
        return False

    # Verifica o tamanho da Pilha
    def length(self):
        return len(self.stack)

#Testes
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.length())