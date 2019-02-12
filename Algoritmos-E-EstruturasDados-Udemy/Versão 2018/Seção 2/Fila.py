class Queue:
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    #Inserir elementos na fila, ao final
    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    #Remover elementos da fila, o inicio
    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    #Verificar o elemento de início da fila
    def front(self):
        if not self.empty():
            return self.queue[0]
        return None


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.front())

'''
FIFO(First in, first out)
O primeiro elemento a entrar, é o primeiro elemento a sair
O pop remove sempre do início da fila, o primeiro que foi inserido.
'''