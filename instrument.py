from generate_id import generate_id

class Instrument:
	"""Instancia novos instrumentos em uma loja especifica
	"""
	def __init__(self, mark: str, model: str, price: float, n_strings):
		"""Instancia um instrumento novo para uma determinada loja

		Args:
			mark (str): marca do instrumento
			model (str): modelo do instrumento
			price (float): preço do instrumento
			n_strings (_type_): numero de cordas do instrumento
		"""
		self.id = generate_id()
		self.mark = mark
		self.model = model
		self. price = price
		self.n_strings = n_strings