import threading
import PySimpleGUI as sg
from PingModel import PingModel

class PingController:
    def __init__(self, destino1, destino2, destino3, num_pings, atraso):
        """
        Inicializa o controlador de ping.

        Args:
        - destino1 (str): O primeiro destino para o teste de ping.
        - destino2 (str): O segundo destino para o teste de ping.
        - destino3 (str): O terceiro destino para o teste de ping.
        - num_pings (int): O número de pings a serem enviados para cada destino.
        - atraso (int): O atraso em segundos entre cada ping.
        """
        self.ping = PingModel()
        self.destino1 = destino1
        self.destino2 = destino2
        self.destino3 = destino3
        self.num_pings = num_pings
        self.atraso = atraso
        self.lock = threading.Lock()  # Lock para sincronização de acesso às variáveis compartilhadas

    def update_progress(self, thread_number, count):
        """
        Atualiza o progresso do ping para uma determinada thread.

        Args:
        - thread_number (int): O número da thread.
        - count (int): O contador de pings para a thread.
        """
        with self.lock:
            if thread_number == 1:
                self.ping.ping_count1 = count
            elif thread_number == 2:
                self.ping.ping_count2 = count
            elif thread_number == 3:
                self.ping.ping_count3 = count

    def run_ping(self):
        """
        Executa o teste de ping.

        Returns:
        - Tuple: Uma tupla contendo os resultados do teste de ping para cada destino.
        """
        # Iniciar as threads de ping
        thread1 = threading.Thread(target=self.ping.ping_test1, args=(self.destino1, self.num_pings, self.atraso, self.update_progress))
        thread2 = threading.Thread(target=self.ping.ping_test2, args=(self.destino2, self.num_pings, self.atraso, self.update_progress))
        thread3 = threading.Thread(target=self.ping.ping_test3, args=(self.destino3, self.num_pings, self.atraso, self.update_progress))

        # Criar a janela de visualização
        layout = [
            [sg.Text("Andamento das Threads")],
            [sg.Text("Thread 1:"), sg.ProgressBar(self.num_pings, orientation='h', size=(50, 20), key='progress1')],
            [sg.Text("Thread 2:"), sg.ProgressBar(self.num_pings, orientation='h', size=(50, 20), key='progress2')],
            [sg.Text("Thread 3:"), sg.ProgressBar(self.num_pings, orientation='h', size=(50, 20), key='progress3')],
            [sg.Button("Fechar")]
        ]
        window = sg.Window("Visualização de Threads", layout)

        # Iniciar as threads de ping
        thread1.start()
        thread2.start()
        thread3.start()

        # Loop de atualização da janela de visualização
        while True:
            event, values = window.read(timeout=100)  # Atualiza a cada 100ms
            if event == sg.WIN_CLOSED or event == "Fechar":
                break
            # Atualizar as barras de progresso com o progresso de cada thread
            with self.lock:
                window['progress1'].update(self.ping.ping_count1)
                window['progress2'].update(self.ping.ping_count2)
                window['progress3'].update(self.ping.ping_count3)

            # Verificar se as barras
            # Verificar se as barras de progresso atingiram 100%
            if self.ping.ping_count1 >= self.num_pings and self.ping.ping_count2 >= self.num_pings and self.ping.ping_count3 >= self.num_pings:
                break

        # Aguardar até que todas as threads terminem
        thread1.join()
        thread2.join()
        thread3.join()
        window.close()

        # Criar uma nova janela indicando que o teste foi finalizado
        layout_final = [
            [sg.Text("Teste Finalizado!")],
            [sg.Button("OK")]
        ]
        window_final = sg.Window("Teste Finalizado", layout_final)
        event, values = window_final.read()
        window_final.close()

        return (
            self.ping.resultados_tempo1,
            self.ping.resultados1,
            self.ping.resultados2,
            self.ping.resultados3
        )

# Exemplo de uso
#if __name__ == "__main__":
    #controller = PingController("destino1", "destino2", "destino3", 5, 1)
    #controller.run_ping()
