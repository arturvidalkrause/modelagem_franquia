import unittest
from store import Loja
from location import Location
from employee import Employee, Positions
from instrument import Instruments, Instrument
from generate_id import generate_id

class TestLocation(unittest.TestCase):
    def test_location_creation(self):
        location = Location("12345-678", "Rua Exemplo", 100)
        self.assertEqual(location.cep, "12345-678")
        self.assertEqual(location.street, "Rua Exemplo")
        self.assertEqual(location.number, 100)

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee("João", 12345678901, 3000.0, Positions.SALES_ASSOCIATE, generate_id())
        self.assertEqual(employee.name, "João")
        self.assertEqual(employee.document_cpf, 12345678901)
        self.assertEqual(employee.wage, 3000.0)
        self.assertEqual(employee.position, Positions.SALES_ASSOCIATE)

    def test_update_employee_position(self):
        employee = Employee("Maria", 98765432109, 3500.0, Positions.CASHIER, generate_id())
        employee.update_position(Positions.SALES_SUPERVISOR)
        self.assertEqual(employee.position, Positions.SALES_SUPERVISOR)

    def test_update_employee_wage(self):
        employee = Employee("Carlos", 11122233344, 2500.0, Positions.INVENTORY_MANAGER, generate_id())
        employee.update_wage(3000.0)
        self.assertEqual(employee.wage, 3000.0)

class TestInstrument(unittest.TestCase):
    def test_instrument_creation(self):
        instrument = Instrument(generate_id(), Instruments.GUITARRA, "Fender", "Stratocaster", 1500.0, 6)
        self.assertEqual(instrument.name, Instruments.GUITARRA)
        self.assertEqual(instrument.mark, "Fender")
        self.assertEqual(instrument.model, "Stratocaster")
        self.assertEqual(instrument.price, 1500.0)
        self.assertEqual(instrument.n_strings, 6)

class TestLoja(unittest.TestCase):
    def setUp(self):
        self.location = Location("12345-678", "Rua Principal", 500)
        self.store = Loja("Loja Exemplo", self.location, generate_id())

    def test_store_creation(self):
        self.assertEqual(self.store.name, "Loja Exemplo")
        self.assertEqual(self.store.location, self.location)

    def test_add_employee(self):
        employee = Employee("Ana", 22233344455, 3200.0, Positions.CUSTOMER_SERVICE, self.store.id)
        self.store.add_employee(employee)
        self.assertIn(employee.id, self.store.employee)

    def test_remove_employee(self):
        employee = Employee("Lucas", 33344455566, 2900.0, Positions.SALES_ASSOCIATE, self.store.id)
        self.store.add_employee(employee)
        self.store.remove_employee(employee.id)
        self.assertNotIn(employee.id, self.store.employee)

    def test_add_instrument(self):
        self.store.add_instrument("Guitarra", "Ibanez", "RG350", 1200.0, 6)
        instrument_id = next(iter(self.store.stock))
        instrument = self.store.stock[instrument_id]
        self.assertEqual(instrument.name, "Guitarra")
        self.assertEqual(instrument.mark, "Ibanez")

    def test_remove_instrument(self):
        self.store.add_instrument("Violao", "Yamaha", "C40", 800.0, 6)
        instrument_id = next(iter(self.store.stock))
        self.store.remove_instrument(instrument_id)
        self.assertNotIn(instrument_id, self.store.stock)

    def test_update_location(self):
        new_location = Location("98765-432", "Rua Nova", 200)
        self.store.update_location(new_location)
        self.assertEqual(self.store.location, new_location)

    def test_update_nearest_store(self):
        new_nearest_store_id = generate_id()
        self.store.update_nearest_store(new_nearest_store_id)
        self.assertEqual(self.store.nearest_store_id, new_nearest_store_id)

if __name__ == "__main__":
    unittest.main()
