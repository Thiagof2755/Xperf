import time
from datetime import datetime
import speedtest

def run_speed_test_async(stop_event, results_list):
    st = speedtest.Speedtest()
    st.get_best_server()

    while not stop_event.is_set():
        download_speed, upload_speed = run_speed_test(st)
        time_date_speedtest = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        result = {
            'download_speed': download_speed,
            'upload_speed': upload_speed,
            'time_date': time_date_speedtest
        }

        results_list.append(result)

        time.sleep(200)

def run_speed_test(st):
    st.download()
    st.upload()
    st_results = st.results.dict()

    download_speed = st_results["download"] / 1024 / 1024  # Convertendo para Mbps
    upload_speed = st_results["upload"] / 1024 / 1024  # Convertendo para Mbps

    return download_speed, upload_speed
