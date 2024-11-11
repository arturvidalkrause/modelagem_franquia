import enum
from generate_id import generate_id

class Positions(enum.Enum):
	"""Todos os cargos disponíveis

	return:
		CEO (Chief Executive Officer): Responsável pela liderança geral.
		COO (Chief Operations Officer): Supervisiona operações das lojas.
		REGIONAL_MANAGER (Regional Manager): Gerencia várias lojas em uma região.
		STORAGE_MANAGER (Store Manager): Gerente da loja, responsável pela operação diária.
		SALES_SUPERVISOR (Sales Supervisor): Supervisiona a equipe de vendas e o atendimento ao cliente.
		INVENTORY_MANAGER (Inventory Manager): Cuida do estoque e organização.
		SALES_ASSOCIATE (Sales Associate): Vendedor que atende clientes e realiza vendas.
		INSTRUMENT_SPECIALIST (Instrument Specialist): Especialista em instrumentos específicos.
		CASHIER (Cashier): Responsável pelo caixa e pagamentos.
		CUSTOMER_SERVICE (Customer Service Representative): Atendimento ao cliente para suporte e trocas.
	"""
	CEO = enum.auto()
	COO = enum.auto()
	REGIONAL_MANAGER = enum.auto()
	STORAGE_MANAGER = enum.auto()
	SALES_SUPERVISOR = enum.auto()
	INVENTORY_MANAGER = enum.auto()
	SALES_ASSOCIATE = enum.auto()
	INSTRUMENT_SPECIALIST = enum.auto()
	CASHIER = enum.auto()
	CUSTOMER_SERVICE = enum.auto()

class Employee:
	"""Instancia um novo funcionario
	"""
	def __init__(self, name: str, document_cpf: int, wage: float, position: Positions, current_store_id: hex):
		"""Instancia um novo funcionario

		Args:
			name (str): nome do funcionario
			document_cpf (int): docummento(CPF) do funcionario
			wage (float): salario recebido pelo funcionario
			position (Positions): cargo assumido pelo funcionario
			current_store_id (hex): loja em que o funcionario trabalha

		Raises:
			ValueError: Cargo não encontrado
		"""
		if not isinstance(position, Positions):
			raise ValueError(f"{position} is not found")
		
		self.id = generate_id()
		self.name = name
		self.document_cpf = document_cpf
		self.wage = wage
		self.position = position
		self.current_store_id = current_store_id

	def update_current_store(self, new_current_store_id: hex):
		"""Transfere o funcionario

		Args:
			new_current_store_id (hex): id da loja para o qual o funcionario sera transferido
		"""
		self.current_store_id = new_current_store_id

	def update_position(self, new_position: Positions):
		"""Altera o cargo que o funcionario exerce dentro da franquia

		Args:
			new_position (Positions: Novo cargo que o funcionario exercerá

		Raises:
			ValueError: Novo cargo não encontrado
		"""
		if not isinstance(new_position, Positions):
			raise ValueError(f"{new_position} is not found.")
		
		self.position = new_position

	def update_wage(self, new_wage: float):
		"""Atualiza o salario do funcionario

		Args:
			new_wage (float): novo salario do funcionario
		"""
		self.wage = new_wage