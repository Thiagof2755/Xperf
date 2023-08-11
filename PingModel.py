import ping3
import time

class PingModel:
    @staticmethod    
    def ping_test1(destino1, num_pings, atraso):
        resultados_tempo = []
        resultados1 = []
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino1)
            tempo_atual = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if tempo_resposta is None or tempo_resposta >= 500:
                tempo_resposta = -0.01
            resultados_tempo.append(tempo_atual)
            resultados1.append(int(tempo_resposta * 1000))
            time.sleep(atraso)
        return resultados_tempo, resultados1

    def ping_test2(self, destino2, num_pings, atraso):
        resultados2 = []
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino2)
            if tempo_resposta is None or tempo_resposta >= 500:
                tempo_resposta = -0.01
            resultados2['ms'].append(int(tempo_resposta * 1000))
            time.sleep(atraso)
        return resultados2

    def ping_test3(self, destino3, num_pings, atraso):
        resultados3 = []
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino3)
            if tempo_resposta is None or tempo_resposta >= 500:
                tempo_resposta = -0.01
            resultados3['ms'].append(int(tempo_resposta * 1000))
            time.sleep(atraso)
        return resultados3