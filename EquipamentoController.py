from View import View


class EquipamentoController:
    def __init__(self):
        self.view = View()

    def run(self):
        return self.view.input_equipment_info()
