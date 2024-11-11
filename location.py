class Location:
	def __init__(self, cep: str, street: str, number: int):
		"""instancia uma nova localização

		Args:
			cep (str): Codigo postal da localização
			street (str): nome da rua
			number (int): numero do estabelecimento
		"""
		self.cep = cep
		self.street = street
		self.number = number