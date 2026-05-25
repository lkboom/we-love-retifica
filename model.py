# model.py
lista_clientes = []
lista_motores = []
lista_cabecotes = []


class Cliente:
    def __init__(self, nome, telefone, cpf, cidade, tipo_servico):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cidade = cidade
        self.tipo_servico = tipo_servico


class Motor:
    def __init__(self, modelo, ano, servico):
        self.modelo = modelo
        self.ano = ano
        self.servico = servico

class Bloco(Motor):
    def __init__(self, modelo, ano, servico, cilindrada ):
        super().__init__(modelo, ano, servico)
        self.cilindrada = cilindrada


class Cabecote(Motor):
    def __init__(self, modelo, ano, servico,combustivel, ponto_zero):
        super().__init__(modelo, ano, servico)
        self.combustivel = combustivel
        self.ponto_zero = ponto_zero


class Retifica:
    def __init__(self, nome='RETPARTS'):
        self.nome = nome
        self.clientes = []
        self.blocos = []
        self.cabecotes = []


    def cad_cliente(self,cliente):

        self.clientes.append(cliente)

    def cad_motor(self,bloco):

        self.blocos.append(bloco)

    def cad_cabecote(self,cabecote):
        self.cabecotes.append(cabecote)
