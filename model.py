class Cliente:
    def __init__(self, nome, telefone, cpf, city):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cidade = city

class Motor:
    def __init__(self, modelo, ano, cilindrada, tipo_servico):
        self.modelo = modelo
        self.ano = ano
        self.cilindrada = cilindrada
        self.tipo_servico = tipo_servico
        
        
class Retifica:
    def __init__(self, nome = 'RETPARTS'):
        self.clientes = []
        self.motores = []