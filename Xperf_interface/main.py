import threading
from View import View
from database_functions import EquipmentInfo
from SpeedTestController import SpeedTestController
from datetime import datetime
from SpeedTestModel import SpeedTestModel
import speedtest

# Variável de evento para sinalizar a interrupção da thread de teste de velocidade
stop_speed_test_event = threading.Event()

def run_speed_tests(speed_test_model):
    """
    Função que executa os testes de velocidade usando um objeto SpeedTestModel.
    """
    global speed_test_results

    try:
        speed_test_model.run_speed_tests(stop_speed_test_event)  # Passando stop_speed_test_event
        if stop_speed_test_event.is_set():
            print("Thread de teste de velocidade interrompida.")
            return
    except speedtest.ConfigRetrievalError as e:
        print("Erro ao obter configuração para o teste de velocidade:", e)

if __name__ == "__main__":
    # Configurações do banco de dados
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'xperf'

    interval = 4000
    repetitions = 20

    # Criar uma instância da classe SpeedTestModel
    speed_test_model = SpeedTestModel(interval, repetitions)

    # Criar uma thread para executar os testes de velocidade
    speed_test_thread = threading.Thread(target=run_speed_tests, args=(speed_test_model,))
    speed_test_thread.start()

    # Criar uma instância da classe View
    view = View()
    
    # Chamar o método input_equipment_info para obter informações do equipamento
    modelo, marca_selecionada, mac = view.input_equipment_info()

    # Chamar o método Ping da classe View para obter os resultados do teste de ping
    resultados_tempo1, resultados1, resultados2, resultados3 = view.Ping()
    
    # Sinalizar a interrupção da thread de teste de velocidade após a função view.Ping() terminar
    stop_speed_test_event.set()

    # Aguardar a conclusão da thread de teste de velocidade
    speed_test_thread.join()

    # Criar uma instância da classe EquipmentInfo
    Banco = EquipmentInfo(host, user, password, database)
    
    # Criar uma tupla com as informações do equipamento
    equipment_info = (modelo, marca_selecionada, mac)
    ping_results = []

    # Adicione todos os elementos dos arrays resultados1, resultados2 e resultados3 à lista ping_results
    for i in range(len(resultados1)):
        ping_results.append((resultados1[i], resultados2[i], resultados3[i], resultados_tempo1[i]))
    
    # Lista para armazenar os resultados dos testes de velocidade
    speed_results = []

    # Adicione os resultados dos testes de velocidade à lista speed_results
    for result in speed_test_model.get_test_results():
        speed_results.append(result)

    # Inserir resultados de teste de velocidade na tabela 'speedtest'
    for result in speed_results:
        download_speed = result["Velocidade de Download"]
        upload_speed = result["Velocidade de Upload"]
        speed_time = result["Hora"]
        
        # Inserir dados na tabela 'speedtest'
        Banco.insert_data_to_db(equipment_info, ping_results, download_speed, upload_speed, speed_time)

    # Imprimir informações sobre o equipamento
    print(modelo) 
    print(marca_selecionada)
    print(mac)
    print(resultados_tempo1)    
    print(resultados1)
    print(resultados2)
    print(resultados3)

    # Imprimir resultados dos testes de velocidade
    print("\nResultados dos testes de velocidade:")
    for result in speed_results:
        print("Hora:", result["Hora"])
        print("Velocidade de Download:", result["Velocidade de Download"], "Mbps")
        print("Velocidade de Upload:", result["Velocidade de Upload"], "Mbps")
        print()
