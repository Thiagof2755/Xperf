import threading
from SpeedTestModel import SpeedTestModel

class SpeedTestController:
    def __init__(self, interval, repetitions):
        self.interval = interval
        self.repetitions = repetitions

    def run_speed_tests(self, stop_event):
        speed_test_model = SpeedTestModel(self.interval, self.repetitions)
        speed_test_model.run_speed_tests(stop_event)  # Passando stop_event para o método
        return speed_test_model.get_test_results()
