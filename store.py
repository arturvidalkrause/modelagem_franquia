from instrument import Instrument, Instruments
from generate_id import generate_id

class Loja:
	"""Classe destinada a instanciar uma nova loja, e seas atualizações
	"""
	def __init__(self, name: str, location: object, nearest_store: str) -> None:
		"""Instancia a Loja

		Args:
			id (hex): id unico de cada loja
			name (str): nome da loja
			location (object): localização da loja
			nearest_store (str): loja mais próxima
		"""
		self.id = generate_id()
		self.name = name
		self.location = location
		self.nearest_store_id = nearest_store
		self.employee = {}
		self.stock = {}

	def add_employee(self, employee: object):
		"""Adicina um novo funcionário

		Args:
			employee (object): Novo funcionário
		"""
		self.employee[employee.id] = employee
		print(f"Funcionário contratado:", employee.id)

	def find_employee(self, id: hex) -> object:
		"""Procura um funcionário cadastrado

		Args:
			id (hex): id do funcionário a ser procurado

		Returns:
			object: funcionario encontrado
		"""
		return self.employee[id]

	def remove_employee(self, employee_id: hex):
		"""Remove um funcionário

		Args:
			employee_id (hex): id do funcionario a ser demitido
		"""
		del self.employee[employee_id]
		print(f"Funcionário demitido:", employee_id)

	def update_location(self, new_location: object):
		"""Atualiza a localização da loja caso seja transferiada para outra região

		Args:
			new_location (object): nova localização da loja
		"""
		self.location = new_location
		print(f"Localização atualizada:", new_location)

	def add_instrument(self, name: str, mark: str, model: str, price: float, number_of_string: int):
		"""Adiciona um novo instrumento

		Args:
			name (str): nome do instrumento
			mark (str): marca do instrumento
			model (str): modelo do instrumento
			price (float): preço do instrumento
			number_of_string (int): numero de cordas do instrumento
		"""
		try:
			instrument_name = Instruments[name.upper()]  # Converte o nome para o enum
		except KeyError:
			raise ValueError(f"{name} is not a valid instrument name.")
        
		self.stock[id] = Instrument(id, instrument_name, mark, model, price, number_of_string)
		print(f"Instrumento cadastrado:", id)

	def find_instrument(self, id: hex) -> object:
		"""Procura um funcionário cadastrado

		Args:
			id (hex): id do funcionário a ser procurado

		Returns:
			object: intrumento encontrado
		"""
		return self.stock[id]

	def remove_instrument(self, id_instrument: hex):
		"""Remove um instrumento do estoque

		Args:
			id_instrument (hex): id do instrumento a ser removido
		"""
		del self.stock[id_instrument]
		print(f"Instrumento vendido:", id_instrument)
	
	def update_nearest_store(self, new_nearest_store_id: hex):
		"""Atualiza a loja loja mais proxima

		Args:
			new_nearest_store_id (hex): id da loja mais proxima
		"""
		self.nearest_store_id = new_nearest_store_id
		print(f"Localização da loja mais próxima atualizada:", new_nearest_store_id)
		