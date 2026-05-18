class Cliente:
    def __init__(self, nome, telefone, cpf, city, tipo_servico):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cidade = city
        self.tipo_servico = tipo_servico

    def exibir_dados(self):
        print("DADOS DO CLIENTE")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CPF: {self.cpf}")
        print(f"Cidade: {self.cidade}")
        print(f"Serviço solicitado: {self.tipo_servico}")

class Motor:
    def __init__(self, modelo, ano, cilindrada):
        self.modelo = modelo
        self.ano = ano
        self.cilindrada = cilindrada

    def exibir_dados(self):
        print("DADOS DO MOTOR")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cilindrada: {self.cilindrada}")
     