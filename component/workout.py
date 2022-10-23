class Workout:
    def __init__(self, name, units, amount, difficulty):
        self.name = name
        self. units = units
        self.amount = amount
        self.difficulty = difficulty

    def print_info(self):
        print(f'{self.name} for {self.amount} {self.units}. Worth {self.difficulty} points.')