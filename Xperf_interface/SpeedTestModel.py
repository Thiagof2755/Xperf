import speedtest
import time
from datetime import datetime

class SpeedTestModel:
    def __init__(self, interval, repetitions):
        """
        Inicializa uma instância da classe SpeedTestModel.

        Args:
            interval (int): O intervalo de tempo, em segundos, entre cada teste de velocidade.
            repetitions (int): O número de repetições de teste de velocidade a serem executadas.
        """
        self.interval = interval
        self.repetitions = repetitions
        self.test_times = []
        self.download_speeds = []
        self.upload_speeds = []

    def run_speed_tests(self, stop_event):
        """
        Executa os testes de velocidade de download e upload.

        Args:
            stop_event (threading.Event): O evento para sinalizar a interrupção do loop de testes.

        Returns:
            None
        """
        st = speedtest.Speedtest()

        for i in range(self.repetitions):
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            download_speed = st.download() / 10**6  # Convert to Mbps
            upload_speed = st.upload() / 10**6  # Convert to Mbps

            self.test_times.append(current_time)
            self.download_speeds.append(download_speed)
            self.upload_speeds.append(upload_speed)

            if i < self.repetitions - 1:
                time.sleep(self.interval)

            if stop_event.is_set():
                break

    def get_test_results(self):
        """
        Obtém os resultados dos testes de velocidade.

        Returns:
            list: Uma lista de dicionários contendo os resultados dos testes de velocidade.
        """
        results = []
        num_results = len(self.test_times)

        for i in range(num_results):
            result = {
                "Hora": self.test_times[i],
                "Velocidade de Download": int(self.download_speeds[i]),
                "Velocidade de Upload": int(self.upload_speeds[i])
            }
            results.append(result)
        return results
