import enum

class Instruments(enum.Enum):
	BAIXO = enum.auto()
	GUITARRA = enum.auto()
	VIOLAO = enum.auto()

class Instrument:
	"""Instancia novos instrumentos em uma loja especifica
	"""
	def __init__(self, id: hex, name: Instruments, mark: str, model: str, price: float, n_strings):
		"""Instancia um instrumento novo para uma determinada loja

		Args:
			id (hex): id do instrumento que e fornecida ao der instanciada pela loja
			name (Instruments): nome do instrumento
			mark (str): marca do instrumento
			model (str): modelo do instrumento
			price (float): preço do instrumento
			n_strings (_type_): numero de cordas do instrumento

		Raises:
			ValueError: Nome do instrumento não encontrado
		"""
		if not isinstance(name, Instruments):
			raise ValueError(f"{name} is not found")
		self.id = id
		self.name = name
		self.mark = mark
		self.model = model
		self. price = price
		self.n_strings = n_strings