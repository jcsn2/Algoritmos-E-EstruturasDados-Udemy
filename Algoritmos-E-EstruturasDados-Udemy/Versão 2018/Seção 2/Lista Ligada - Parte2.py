class Node:

	def __init__(self, label):
		self.label = label
		self.next = None

    #Retorna o nome do nó
	def getLabel(self):
		return self.label

    #Seta o nome do nó
	def setLabel(self, label):
		self.label = label

    #Retornar a referência (o próximo)
	def getNext(self):
		return self.next

    #Seta a referência (o próximo)
	def setNext(self, next):
		self.next = next


class LinkedList:

	def __init__(self):
		self.first = None #Referência do primeiro elemento
		self.last = None #Referência do último elemento
		self.len_list = 0

    #Inserir na lista
	def push(self, label, index):

		if index >= 0:

			# cria o novo o nó
			node = Node(label)

			# verifica se a lista está vazia
			if self.empty():
				self.first = node
				self.last = node
			else:

				if index == 0:
					# inserção no início
					node.setNext(self.first)
					self.first = node
				elif index >= self.len_list:
					# inserção no final
					self.last.setNext(node)
					self.last = node
				else:
					# inserção no meio
					prev_node = self.first
					curr_node = self.first.getNext()
					curr_index = 1

					while curr_node != None:

						if curr_index == index:
							# seta o curr_node como o próximo do nó
							node.setNext(curr_node)
							# seta o node como o próximo do prev_node
							prev_node.setNext(node)
							break

						prev_node = curr_node
						curr_node = curr_node.getNext()
						curr_index += 1

					# atualiza o tamanho da lista
					self.len_list += 1