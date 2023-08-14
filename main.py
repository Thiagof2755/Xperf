from View import View
from database_functions import EquipmentInfo

if __name__ == "__main__":
    # Configurações do banco de dados
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'xperf'

    view = View()  # Criar uma instância da classe View
    modelo, marca_selecionada, mac = view.input_equipment_info()  # Chamar o método input_equipment_info

    resultados_tempo1, resultados1, resultados2, resultados3 =  view.Ping()
    print(modelo) 
    print(marca_selecionada)
    print(mac)
    print(resultados_tempo1)    
    print(resultados1)
    print(resultados2)
    print(resultados3)

      
    
    Banco = EquipmentInfo(host, user, password, database)
    # Chame o método insert_data_to_db com todos os parâmetros necessários
    equipment_info = (modelo, marca_selecionada, mac)
    ping_results = []

    # Adicione todos os elementos dos arrays resultados1, resultados2 e resultados3 à lista ping_results
    for i in range(len(resultados1)):
        ping_results.append((resultados1[i], resultados2[i], resultados3[i], resultados_tempo1[i]))

    Banco.insert_data_to_db(equipment_info, ping_results)