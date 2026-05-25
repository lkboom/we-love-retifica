from model import *

class UI:
    
    def __init__(self, retifica):
        self.retifica = retifica

    def cad_cliente(self):
        print("\n--- CADASTRO DE CLIENTE ---")
        nome         = input('Qual o nome do cliente? ')
        telefone     = input('Qual o telefone do cliente? ')
        cpf          = input('Qual o CPF do cliente? ')
        cidade       = input('Em que cidade o cliente mora? ')

        print('\nQual o tipo de serviço?')
        print('1 - Motor')
        print('2 - Cabeçote')
        opcao = input('Digite 1 ou 2: ')

        if opcao == '1':
            tipo_servico = 'Motor'
        elif opcao == '2':
            tipo_servico = 'Cabeçote'
        else:
            print('Opção inválida, definido como Motor.')
            tipo_servico = 'Motor'

        if tipo_servico == 'Motor':
            self.cad_motor()
        else:
            self.cad_cabecote()

    def cad_motor(self):
        print("\n--- CADASTRO DE MOTOR ---")
        modelo       = input('Qual o modelo do motor? ')
        ano          = input('Qual o ano do motor? ')
        cilindrada   = input('Qual a cilindrada do motor? ')
        tipo_servico = input('Qual serviço será feito? ')

        print("\n--- CADASTRO DE CABEÇOTE ---")
        tipo = input('Qual o tipo do cabeçote? (ex: 4 cilindros, 6 cilindros) ')

        print('Qual o combustível?')
        print('1 - Gasolina')
        print('2 - Diesel')
        opcao = input('Digite 1 ou 2: ')
        combustivel = 'Gasolina' if opcao == '1' else 'Diesel'

        print('É ponto zero?')
        print('1 - Sim')
        print('2 - Não')
        opcao = input('Digite 1 ou 2: ')
        ponto_zero = 'Sim' if opcao == '1' else 'Não'

        ano     = input('Qual o ano? ')
        servico = input('Qual serviço será feito? ')

    def exibir_cliente(self, cliente):
        print("\nDADOS DO CLIENTE")
        print(f"Nome: {cliente.nome}")
        print(f"Telefone: {cliente.telefone}")
        print(f"CPF: {cliente.cpf}")
        print(f"Cidade: {cliente.cidade}")
        print(f"Serviço solicitado: {cliente.tipo_servico}")

    def exibir_motor(self, motor):
        print("\nDADOS DO MOTOR")
        print(f"Modelo: {motor.modelo}")
        print(f"Ano: {motor.ano}")
        print(f"Cilindrada: {motor.cilindrada}")
        print(f"Serviço solicitado: {motor.tipo_servico}")

    def exibir_cabecote(self, cabecote):
        print("\nDADOS DO CABEÇOTE")
        print(f"Tipo: {cabecote.tipo}")
        print(f"Combustível: {cabecote.combustivel}")
        print(f"Ponto zero: {cabecote.ponto_zero}")
        print(f"Ano: {cabecote.ano}")
        print(f"Serviço solicitado: {cabecote.servico}")

    def listar_clientes(self):
        if not self.retifica.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for cliente in self.retifica.clientes:
            self.exibir_cliente(cliente)

    def listar_motores(self):
        if not self.retifica.motores:
            print("Nenhum motor cadastrado.")
            return
        for motor in self.retifica.motores:
            self.exibir_motor(motor)

    def listar_cabecotes(self):
        if not self.retifica.cabecotes:
            print("Nenhum cabeçote cadastrado.")
            return
        for cabecote in self.retifica.cabecotes:
            self.exibir_cabecote(cabecote)
    def __init__(self, retifica):
        self.retifica = retifica

    def cad_cliente(self):
        print("\n--- CADASTRO DE CLIENTE ---")
        nome         = input('Qual o nome do cliente? ')
        telefone     = input('Qual o telefone do cliente? ')
        cpf          = input('Qual o CPF do cliente? ')
        cidade       = input('Em que cidade o cliente mora? ')

        print('\nQual o tipo de serviço?')
        print('1 - Motor')
        print('2 - Cabeçote')
        opcao = input('Digite 1 ou 2: ')

        if opcao == '1':
            tipo_servico = 'Motor'
        elif opcao == '2':
            tipo_servico = 'Cabeçote'
        else:
            print('Opção inválida, definido como Motor.')
            tipo_servico = 'Motor'


        if tipo_servico == 'Motor':
            self.cad_motor()
        else:
            self.cad_cabecote()

    def cad_motor(self):
        print("\n--- CADASTRO DE MOTOR ---")
        modelo       = input('Qual o modelo do motor? ')
        ano          = input('Qual o ano do motor? ')
        cilindrada   = input('Qual a cilindrada do motor? ')
        tipo_servico = input('Qual serviço será feito? ')


    def cad_cabecote(self):
        print("\n--- CADASTRO DE CABEÇOTE ---")
        tipo = input('Qual o tipo do cabeçote? (ex: 4 cilindros, 6 cilindros) ')

        print('Qual o combustível?')
        print('1 - Gasolina')
        print('2 - Diesel')
        opcao = input('Digite 1 ou 2: ')
        combustivel = 'Gasolina' if opcao == '1' else 'Diesel'

        print('É ponto zero?')
        print('1 - Sim')
        print('2 - Não')
        opcao = input('Digite 1 ou 2: ')
        ponto_zero = 'Sim' if opcao == '1' else 'Não'

        ano     = input('Qual o ano? ')
        servico = input('Qual serviço será feito? ')


    def exibir_cliente(self, cliente):
        print("\nDADOS DO CLIENTE")
        print(f"Nome: {cliente.nome}")
        print(f"Telefone: {cliente.telefone}")
        print(f"CPF: {cliente.cpf}")
        print(f"Cidade: {cliente.cidade}")
        print(f"Serviço solicitado: {cliente.tipo_servico}")

    def exibir_motor(self, motor):
        print("\nDADOS DO MOTOR")
        print(f"Modelo: {motor.modelo}")
        print(f"Ano: {motor.ano}")
        print(f"Cilindrada: {motor.cilindrada}")
        print(f"Serviço solicitado: {motor.tipo_servico}")

    def exibir_cabecote(self, cabecote):
        print("\nDADOS DO CABEÇOTE")
        print(f"Tipo: {cabecote.tipo}")
        print(f"Combustível: {cabecote.combustivel}")
        print(f"Ponto zero: {cabecote.ponto_zero}")
        print(f"Ano: {cabecote.ano}")
        print(f"Serviço solicitado: {cabecote.servico}")

    def listar_clientes(self):
        if not self.retifica.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for cliente in self.retifica.clientes:
            self.exibir_cliente(cliente)

    def listar_motores(self):
        if not self.retifica.motores:
            print("Nenhum motor cadastrado.")
            return
        for motor in self.retifica.motores:
            self.exibir_motor(motor)

    def listar_cabecotes(self):
        if not self.retifica.cabecotes:
            print("Nenhum cabeçote cadastrado.")
            return
        for cabecote in self.retifica.cabecotes:
            self.exibir_cabecote(cabecote)