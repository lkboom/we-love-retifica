from model import *
from main import lista_clientes, lista_motores

def cad_cliente():
    # nome, telefone, cpf, city, 
    
    nome = input('Qual o nome do cliente? ')
    telefone = input('Qual o telefone do cliente? ')
    cpf = input('Qual o cpf do cliente? ')
    city = input('Em que cidade o cliente mora? ')
    
    lista_clientes.append(Cliente)
    exibir_cliente(Cliente)
    
def cad_motor():
    # modelo, ano, cilindrada tipo_servico
    
    modelo = input('Qual o motor? ')
    modelo = input('Qual o ano do motor? ')
    modelo = input('Qual a cilindrada motor? ')
    tipo_serviço = input('Qual serviço necessário? ')
    
    lista_motores.append(Motor)
    exibir_motor(Motor)
    
def exibir_cliente(cliente):
    print("DADOS DO CLIENTE")
    print(f"Nome: {cliente.nome}")
    print(f"Telefone: {cliente.telefone}")
    print(f"CPF: {cliente.cpf}")
    print(f"Cidade: {cliente.cidade}")

def exibir_motor(motor):
    print("DADOS DO MOTOR")
    print(f"Modelo: {motor.modelo}")
    print(f"Ano: {motor.ano}")
    print(f"Cilindrada: {motor.cilindrada}")
    print(f"Serviço solicitado: {motor.tipo_servico}")

# def rem_cliente():
# def rem_cliente():
# def exibir():