from PingModel import PingModel
import threading


class PingController:
    def __init__(self, destino1, destino2, destino3, num_pings, atraso):
        self.ping = PingModel()
        self.destino1 = destino1
        self.destino2 = destino2
        self.destino3 = destino3
        self.num_pings = num_pings
        self.atraso = atraso

    def run_ping(self):
        # Criar as threads
        thread1 = threading.Thread(target=self.ping.ping_test1, args=(self.destino1, self.num_pings, self.atraso))
        thread2 = threading.Thread(target=self.ping.ping_test2, args=(self.destino2, self.num_pings, self.atraso))
        thread3 = threading.Thread(target=self.ping.ping_test3, args=(self.destino3, self.num_pings, self.atraso))

        # Iniciar as threads
        thread1.start()
        thread2.start()
        thread3.start()

        # Aguardar até que todas as threads terminem
        thread1.join()
        thread2.join()
        thread3.join()

        return (
            self.ping.resultados_tempo1,
            self.ping.resultados1,
            self.ping.resultados2,
            self.ping.resultados3
        )
