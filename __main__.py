import PySimpleGUI as sg
from layout import *
import sys


paginas = Paginas()
window = paginas.tela_principal()

while True:
        
    event, values = window.read()
        
    # See if user wants to quit or window was closed
        
    if event == sg.WINDOW_CLOSED or event == 'Sair':      
        break

    if event == "Cancelar" or event == "Voltar":
        window.close()
        window = paginas.tela_principal()

    if event == "Cadastrar":
        window.close()
        window = paginas.tela_cadastro()

    # Output a message to the window

# Finish up by removing from the screen
window.close()
sys.exit()