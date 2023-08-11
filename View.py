import PySimpleGUI as sg
from PingController import run_ping

class View:

    def __init__(self):
        self.marcas = ['Tenda', 'Huawei', 'Intelbras', 'Tp-Link']

    def input_equipment_info(self):

        sg.theme('DarkBlue13')
        layout = [
            [sg.Text('Equipamento')],
            [sg.Radio(marca, 'marca', key=marca) for marca in self.marcas],
            [sg.Text('Modelo'), sg.InputText(key='modelo')],
            [sg.Text('MAC'), sg.InputText(key='mac')],
            [sg.Button('Iniciar Testes')],
            [sg.Button('Sair')]
        ]

        self.window = sg.Window('Informações do Equipamento', layout, icon='D:\Thiago\Desktop\XPERF\Xperf_IC.ico')

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'Sair':
                self.window.close()
                return 0
            elif event == 'Iniciar Testes':
                modelo = values['modelo']
                marca_selecionada = None
                for marca in self.marcas:
                    if values[marca]:
                        marca_selecionada = marca
                        break
                mac = values['mac']
                self.window.close()
                return modelo, marca_selecionada, mac
    
    def input_destination_info(self):
        sg.theme('DarkBlue13')
    
        layout = [
            [sg.Text('Digite os endereços de destino:')],
            [sg.InputText(key='dest1')],
            [sg.InputText(key='dest2')],
            [sg.InputText(key='dest3')],
            [sg.Text('Digite o número de pings para todos os destinos:')],
            [sg.InputText('', key='num_pings')],
            [sg.Text('Digite o valor do atraso:')],
            [sg.InputText('', key='atraso')],
            [sg.Button('Retornar valores'), sg.Button('Sair')]
        ]
    
        window = sg.Window('Ping Tool', layout)
    
        destinations = []
        num_pings = None
        atraso = None
    
        while True:
            event, values = window.read()
    
            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            elif event == 'Retornar valores':
                # Verifique se todos os campos estão preenchidos
                if all([values['dest1'], values['dest2'], values['dest3'], values['num_pings'], values['atraso']]):
                    destinations = [values['dest1'], values['dest2'], values['dest3']]
                    num_pings_str = values['num_pings']
                    atraso_str = values['atraso']
    
                    # Verifique se o valor de num_pings é um número inteiro
                    try:
                        num_pings = int(num_pings_str)
                        atraso = int(atraso_str)
                    except ValueError:
                        sg.popup('Por favor, insira um valor inteiro para o número de pings e o atraso.')
                        continue  # Volta ao início do loop para aguardar nova entrada
    
                    run_ping(destinations, num_pings, atraso)
                    window.close()
                else:
                    sg.popup('Por favor, preencha todos os campos!')
    
        window.close()
    
    