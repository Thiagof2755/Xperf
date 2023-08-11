from View import View


if __name__ == "__main__":
    # Configurações do banco de dados
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'xperf'

    view = View()  # Criar uma instância da classe View
    equip_info = view.input_equipment_info()  # Chamar o método input_equipment_info