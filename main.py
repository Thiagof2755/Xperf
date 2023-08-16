from View import View
from database_functions import EquipmentInfo
from SpeedTestContoller import SpeedTestController

# Definir a classe SpeedTestController e SpeedTestModel (conforme explicado anteriormente)

if __name__ == "__main__":
    # Configurações do banco de dados
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'xperf'

    view = View()  # Criar uma instância da classe View
    modelo, marca_selecionada, mac = view.input_equipment_info()  # Chamar o método input_equipment_info

    resultados_tempo1, resultados1, resultados2, resultados3 = view.Ping()
    
    # Chamada ao Controller para os testes de velocidade
    controller = SpeedTestController(interval=30, repetitions=2)
    speed_test_results = controller.run_speed_tests()
    
    # Exibir resultados dos testes de velocidade
    for result in speed_test_results:
        print("Hora:", result["Hora"])
        print("Velocidade de Download:", result["Velocidade de Download"], "Mbps")
        print("Velocidade de Upload:", result["Velocidade de Upload"], "Mbps")
        print()
    
    Banco = EquipmentInfo(host, user, password, database)
    
    equipment_info = (modelo, marca_selecionada, mac)
    ping_results = []

    # Adicione todos os elementos dos arrays resultados1, resultados2 e resultados3 à lista ping_results
    for i in range(len(resultados1)):
        ping_results.append((resultados1[i], resultados2[i], resultados3[i], resultados_tempo1[i]))

    # Adicione os resultados dos testes de velocidade à lista ping_results
    #for result in speed_test_results:
    #ping_results.append((result["Velocidade de Download"], result["Velocidade de Upload"], result["Hora"]))

    Banco.insert_data_to_db(equipment_info, ping_results)
    
    print(modelo) 
    print(marca_selecionada)
    print(mac)
    print(resultados_tempo1)    
    print(resultados1)
    print(resultados2)
    print(resultados3)
