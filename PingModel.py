# PingModel.py
import ping3
import time

class PingModel:
    def __init__(self):
        self.resultados_tempo1 = []
        self.resultados1 = []
        self.resultados2 = []
        self.resultados3 = []
        self.ping_count1 = 0  # Progresso da Thread 1
        self.ping_count2 = 0  # Progresso da Thread 2
        self.ping_count3 = 0  # Progresso da Thread 3

    def ping_test1(self, destino1, num_pings, atraso, progress_callback):
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino1)
            tempo_atual = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if tempo_resposta is False or tempo_resposta >= 500:
                tempo_resposta = -0.001
            self.resultados_tempo1.append(tempo_atual)
            self.resultados1.append(int(tempo_resposta * 1000))
            self.ping_count1 += 1  # Atualizar o progresso da Thread 1
            progress_callback(1, self.ping_count1)  # Atualizar progresso na GUI
            time.sleep(atraso)

    def ping_test2(self, destino2, num_pings, atraso, progress_callback):
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino2)
            if tempo_resposta is False or tempo_resposta >= 500:
                tempo_resposta = -0.001
            self.resultados2.append(int(tempo_resposta * 1000))
            self.ping_count2 += 1  # Atualizar o progresso da Thread 2
            progress_callback(2, self.ping_count2)  # Atualizar progresso na GUI
            time.sleep(atraso)

    def ping_test3(self, destino3, num_pings, atraso, progress_callback):
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino3)
            if tempo_resposta is False or tempo_resposta >= 500:
                tempo_resposta = -0.001
            self.resultados3.append(int(tempo_resposta * 1000))
            self.ping_count3 += 1  # Atualizar o progresso da Thread 3
            progress_callback(3, self.ping_count3)  # Atualizar progresso na GUI
            time.sleep(atraso)
