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
        resultados2 = {'ms': []}
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino2)
            if tempo_resposta is None or tempo_resposta >= 500:
                tempo_resposta = -0.01
            resultados2['ms'].append(int(tempo_resposta * 1000))
            time.sleep(atraso)
        return resultados2

    def ping_test3(self, destino3, num_pings, atraso):
        resultados3 = {'ms': []}
        for _ in range(num_pings):
            tempo_resposta = ping3.ping(destino3)
            if tempo_resposta is None or tempo_resposta >= 500:
                tempo_resposta = -0.01
            resultados3['ms'].append(int(tempo_resposta * 1000))
            time.sleep(atraso)
        return resultados3


if __name__ == "__main__":
    destino = "example.com"
    num_pings = 5
    atraso = 1

    modelo_ping = PingModel()

    resultados_tempo, resultados1 = modelo_ping.ping_test1(destino, num_pings, atraso)
    print("Resultados do Teste de Ping 1:")
    print("Resultados de Tempo:", resultados_tempo)
    print("Resultados 1:", resultados1)

    destino2 = "google.com"
    resultados2 = modelo_ping.ping_test2(destino2, num_pings, atraso)
    print("\nResultados do Teste de Ping 2:")
    print("Resultados 2:", resultados2)

    destino3 = "github.com"
    resultados3 = modelo_ping.ping_test3(destino3, num_pings, atraso)
    print("\nResultados do Teste de Ping 3:")
    print("Resultados 3:", resultados3)
