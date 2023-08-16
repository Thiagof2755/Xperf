import speedtest
import time
from datetime import datetime

class SpeedTestModel:
    def __init__(self, interval, repetitions):
        self.interval = interval
        self.repetitions = repetitions
        self.test_times = []
        self.download_speeds = []
        self.upload_speeds = []

    def run_speed_tests(self, stop_event):
        st = speedtest.Speedtest()

        for i in range(self.repetitions):
            if stop_event.is_set():
                break  # Interrompe o loop caso o evento seja sinalizado

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            download_speed = st.download() / 10**6  # Convert to Mbps
            upload_speed = st.upload() / 10**6  # Convert to Mbps

            self.test_times.append(current_time)
            self.download_speeds.append(download_speed)
            self.upload_speeds.append(upload_speed)

            if i < self.repetitions - 1:
                time.sleep(self.interval)

    def get_test_results(self):
        results = []
        num_results = len(self.test_times)  # Obter o número de resultados válidos

        for i in range(num_results):
            result = {
                "Hora": self.test_times[i],
                "Velocidade de Download": int(self.download_speeds[i]),
                "Velocidade de Upload": int(self.upload_speeds[i])
            }
            results.append(result)
        return results