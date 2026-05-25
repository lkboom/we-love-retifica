import PySimpleGUI as sg

class Paginas:
    def tela_cadastro(self):

        subcol1 = [
            [sg.Text("CPF do Cliente", expand_x=True)],
            [sg.Input(key='-CPF-', size=(20,1), pad=(0,0),expand_x=True)]
        ]
        subcol2 = [
            [sg.Text("Telefone do Cliente", expand_x=True)],
            [sg.Input(key='-TELEFONE-', size=(20,1), pad=(0,0), expand_x=True)]
        ]

        coluna1 = [
                [sg.Text("Nome do Cliente")],
                [sg.Input(key='-NOME-', size=(30,1))],

                [sg.Column(subcol1, justification="center"), sg.Column(subcol2, justification="center")],

                [sg.Text("Nascimento", expand_x=True)],

                [sg.Input(readonly=True, enable_events=True, key="-NASCIMENTO-", size=(14,1)),
                sg.CalendarButton('Calendar 1', close_when_date_chosen=True, format='%Y-%m-%d', key='Data', default_date_m_d_y=(9,12,2023))],

                [sg.Text(size=(40,1), key='-OUTPUT-')],
                [sg.Button('Ok'), sg.Button('Cancelar')]
                ]

        coluna2 = [[sg.Image(filename="assets/logo.png", key="-EMOJI-", zoom=0.3)]]

        layout  = [[sg.Column(coluna1, justification="center"), sg.Column(coluna2, justification="center")]]
        return sg.Window("Cadastrar", layout)

    def tela_principal(self):
        layout = [

            [sg.Text("Bem vindo ao we_love_retifica")],
            [sg.Button("Cadastrar"), sg.Button("Sair")]

        ]
        return sg.Window("We <3 Retifica", layout)

        

