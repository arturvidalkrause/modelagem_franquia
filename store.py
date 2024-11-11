from instrument import Instrument
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

	def add_employee(self, employee):
		self.employee[employee.id] = employee
		print(f"Funcionário contratado:", employee.id)

	def remove_employee(self, employee_id):
		del self.employee[employee_id]
		print(f"Funcionário demitido:", employee_id)

	def update_location(self, new_location):
		self.location = new_location
		print(f"Localização atualizada:", new_location)

	def add_instrument(self, mark, model, price, number_of_string):
		id = generate_id()
		self.stock[id] = Instrument(mark, model, price, number_of_string)
		print(f"Instrumento cadastrado:", id)

	def remove_instrument(self, id_instrument):
		del self.stock[id_instrument]
		print(f"Instrumento vendido:", id_instrument)
	
	def update_nearest_store(self, new_nearest_store_id):
		self.nearest_store_id = new_nearest_store_id
		print(f"Localização da loja mais próxima atualizada:", new_nearest_store_id)
		