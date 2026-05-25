# main.py

from model import Retifica, Sistema

retifica = Retifica(nome='RETPARTS')
sistema  = Sistema(retifica)

while True:
    print("\n=== RETPARTS ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Listar motores")
    print("4 - Listar cabeçotes")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        sistema.cad_cliente()
    elif opcao == '2':
        sistema.listar_clientes()
    elif opcao == '3':
        sistema.listar_motores()
    elif opcao == '4':
        sistema.listar_cabecotes()
    elif opcao == '0':
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")

    