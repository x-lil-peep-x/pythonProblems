class Person:

    def sign_in(self):
        print('logged in')

    def __init__(self):
        pass


class Wizzard(Person):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of: {self.power}')


class Archer(Person):
    def __init__(self, name, num_arrows):
        super().__init__()
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with: arrows \n Arrows left: {self.num_arrows}')


wizzard = Wizzard('Merlin', 'Fire')
archer = Archer('Robin', 33)
archer.attack()
wizzard.attack()
