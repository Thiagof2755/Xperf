import threading
from ping_functions import ping_destination
from speed_test_functions import run_speed_test_async
from database_functions import input_equipment_info, insert_data_to_db

if __name__ == "__main__":
    # Configurações do banco de dados
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'xperf'

    # Inserir informações do equipamento no banco de dados
    equip_info = input_equipment_info()

    destinations = ["192.168.18.1", "170.245.4.255", "www.google.com"]
    num_pings = 600

    results = []
    speed_test_results = []

    ping_threads = []
    for destination in destinations:
        thread = threading.Thread(target=ping_destination, args=(destination, num_pings, results))
        thread.start()
        ping_threads.append(thread)

    # Criando e iniciando a thread do teste de velocidade
    stop_event = threading.Event()
    speed_thread = threading.Thread(target=run_speed_test_async, args=(stop_event, speed_test_results))
    speed_thread.start()

    # Aguardando o término das threads de ping
    for thread in ping_threads:
        thread.join()

    # Parando a thread do teste de velocidade e aguardando sua finalização
    stop_event.set()
    speed_thread.join()

    # Processando os resultados dos pings
    ms1, ms2, ms3, dt_hr = [], [], [], []

    for result in results:
        if result['destination'] == "192.168.18.1":
            ms1.extend(result['ms'])
            dt_hr.extend(result['dt_hr'])
        elif result['destination'] == "170.245.4.255":
            ms2.extend(result['ms'])
        elif result['destination'] == "www.google.com":
            ms3.extend(result['ms'])

    print("ms1:", ms1)
    print("ms2:", ms2)
    print("ms3:", ms3)
    print("dt_hr:", dt_hr)

    # Processando os resultados do teste de velocidade
    download_speeds = []
    upload_speeds = []
    time_date_speedtests = []

    for result in speed_test_results:
        download_speeds.append(result['download_speed'])
        upload_speeds.append(result['upload_speed'])
        time_date_speedtests.append(result['time_date'])

    print("Download Speeds (Mbps):", download_speeds)
    print("Upload Speeds (Mbps):", upload_speeds)
    print("Data e hora dos testes de velocidade:", time_date_speedtests)

    # Inserir os dados no banco de dados
    insert_data_to_db(host, user, password, database, equip_info, zip(ms1, ms2, ms3, dt_hr), zip(download_speeds, upload_speeds, time_date_speedtests))
