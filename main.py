from store import Loja
from location import Location
from employee import Employee, Positions
from instrument import Instruments, Instrument
from generate_id import generate_id

def main():
    stores = {}

    while True:
        print("\nSistema de Gerenciamento de Loja")
        print("1. Criar nova loja")
        print("2. Adicionar funcionário")
        print("3. Remover funcionário")
        print("4. Adicionar instrumento")
        print("5. Remover instrumento")
        print("6. Procurar funcionário")
        print("7. Procurar instrumento")
        print("8. Atualizar localização da loja")
        print("9. Atualizar loja mais próxima")
        print("10. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == "1":
            # Cria uma nova loja
            name = input("Nome da loja: ")
            cep = input("CEP da loja: ")
            street = input("Rua da loja: ")
            number = int(input("Número da loja: "))
            location = Location(cep, street, number)
            nearest_store = input("ID da loja mais próxima: ")
            store = Loja(name, location, nearest_store)
            stores[store.id] = store
            print(f"Loja criada com ID: {store.id}")

        elif choice == "2":
            # Adiciona um novo funcionario a loja
            store_id = input("ID da loja: ")
            if store_id in stores:
                name = input("Nome do funcionário: ")
                cpf = int(input("CPF do funcionário: "))
                wage = float(input("Salário do funcionário: "))
                print("Cargos disponíveis:")
                for pos in Positions:
                    print(f"{pos.name}")
                position_name = input("Cargo do funcionário: ")
                position = Positions[position_name.upper()]
                employee = Employee(name, cpf, wage, position, store_id)
                stores[store_id].add_employee(employee)
            else:
                print("Loja não encontrada.")

        elif choice == "3":
            # Remove um funcionario especifico da loja funcionário
            store_id = input("ID da loja: ")
            if store_id in stores:
                employee_id = input("ID do funcionário: ")
                stores[store_id].remove_employee(employee_id)
            else:
                print("Loja não encontrada.")

        elif choice == "4":
            # Adiciona um novo instrumento
            store_id = input("ID da loja: ")
            if store_id in stores:
                name = input("Nome do instrumento: ")
                mark = input("Marca do instrumento: ")
                model = input("Modelo do instrumento: ")
                price = float(input("Preço do instrumento: "))
                n_strings = int(input("Número de cordas: "))
                stores[store_id].add_instrument(name, mark, model, price, n_strings)
            else:
                print("Loja não encontrada.")

        elif choice == "5":
            # Remove um  instrumento
            store_id = input("ID da loja: ")
            if store_id in stores:
                instrument_id = input("ID do instrumento: ")
                stores[store_id].remove_instrument(instrument_id)
            else:
                print("Loja não encontrada.")

        elif choice == "6":
            # Procura um funcionario na loja
            store_id = input("ID da loja: ")
            if store_id in stores:
                employee_id = input("ID do funcionário: ")
                employee = stores[store_id].find_employee(employee_id)
                print(f"Funcionário encontrado: {employee.name}, Cargo: {employee.position}")
            else:
                print("Loja não encontrada.")

        elif choice == "7":
            # Procura um instrumento no estoque da loja
            store_id = input("ID da loja: ")
            if store_id in stores:
                instrument_id = input("ID do instrumento: ")
                instrument = stores[store_id].find_instrument(instrument_id)
                print(f"Instrumento encontrado: {instrument.name}, Marca: {instrument.mark}, Preço: {instrument.price}")
            else:
                print("Loja não encontrada.")

        elif choice == "8":
            # Atualiza a localização da loja
            store_id = input("ID da loja: ")
            if store_id in stores:
                cep = input("Novo CEP: ")
                street = input("Nova Rua: ")
                number = int(input("Novo Número: "))
                new_location = Location(cep, street, number)
                stores[store_id].update_location(new_location)
            else:
                print("Loja não encontrada.")

        elif choice == "9":
            # Atualiza a loja que se encontra mais próxima
            store_id = input("ID da loja: ")
            if store_id in stores:
                nearest_store_id = input("Novo ID da loja mais próxima: ")
                stores[store_id].update_nearest_store(nearest_store_id)
            else:
                print("Loja não encontrada.")

        elif choice == "10":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
