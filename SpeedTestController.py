import threading
import PySimpleGUI as sg
from SpeedTestModel import SpeedTestModel

class SpeedTestController:
    def __init__(self, interval, repetitions):
        self.interval = interval
        self.repetitions = repetitions

    def display_progress(self, speed_test_model):
        layout = [
            [sg.Text('Progress:')],
            [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar')],
            [sg.Cancel()]
        ]

        window = sg.Window('Progress', layout)
        progress_bar = window['progressbar']

        while True:
            event, values = window.read(timeout=100)
            if event == 'Cancel' or event == sg.WINDOW_CLOSED:
                break

            progress_value = speed_test_model.get_progress()

            # Update the progress bar
            progress_bar.UpdateBar(progress_value)

            if progress_value == 100:
                break

        window.close()

    def run_speed_tests(self, stop_event):
        speed_test_model = SpeedTestModel(self.interval, self.repetitions)
        self.display_progress(speed_test_model)
        speed_test_model.run_speed_tests(stop_event)


        return speed_test_model.get_test_results()
