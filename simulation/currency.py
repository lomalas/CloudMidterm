class Currency:
    def __init__(self, name, code, base_value=1.0, peg_to=None):
        self.name = name
        self.code = code
        self.value = base_value
        self.peg_to = peg_to

    def update_value(self, change_percent):
        if self.peg_to:
            self.value = self.peg_to.value
        else:
            self.value *= (1 + change_percent)