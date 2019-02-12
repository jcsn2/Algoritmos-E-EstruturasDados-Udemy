class Pessoa:

	def __init__(self):
		self.__nome = None

	@property #Recuperar valor
	def nome(self):
		return self.__nome #Atributo privado sempre vem com __

	@nome.setter #Setar Valor
	def nome(self, nome):
		self.__nome = nome

p = Pessoa()
p.nome = 'Marcos'
print(p.nome)