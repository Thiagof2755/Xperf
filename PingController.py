from PingModel import PingModel
import threading


class PingController:
    def __init__(self):
        self.ping = PingModel()

    def run_ping(self, destino, num_pings, atraso):

        thread1 = threading.Thread(target=self.ping_test1, args=(destino, num_pings, atraso))
        thread2 = threading.Thread(target=self.ping_test2, args=(destino, num_pings, atraso))
        thread3 = threading.Thread(target=self.ping_test3, args=(destino, num_pings, atraso))

        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()

        return thread1, thread2, thread3

 
