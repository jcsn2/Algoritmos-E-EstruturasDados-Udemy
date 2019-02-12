class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    #Inserir na Pilha
    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    #Remover da Pilha
    def pop(self):
        if not self.empty(): #Se a lista não estiver vazia
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    #Saber o elemento do Topo(Último Elemento)
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    #Verificar se a pilha eh vazia
    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    #Verifica o tamanho da Pilha
    def length(self):
        return self.len_stack


s = Stack()
s.push(1)
s.push(2)
s.push(3)
# print(s.top())
s.pop()
# print(s.top())
s.pop()
print(s.length())