import time
from datetime import datetime
from ping3 import ping
from tqdm import tqdm

def ping_destination(destination, num_pings, results_list):
    result = {'destination': destination, 'ms': [], 'dt_hr': []}

    for i in tqdm(range(num_pings), desc=f"Pings para {destination}"):
        try:
            start_time = time.time()
            response_time = ping(destination)
            end_time = time.time()

            elapsed_time = (end_time - start_time) * 1000
            rounded_time = round(elapsed_time)

            result['ms'].append(rounded_time)

            if destination == "192.168.18.1":
                time_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                result['dt_hr'].append(time_date)

        except PermissionError:
            print(f"Acesso negado ao executar ping para {destination}.")

        time.sleep(2)

    results_list.append(result)
