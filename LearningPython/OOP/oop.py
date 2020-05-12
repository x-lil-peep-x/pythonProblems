class Player:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')


class Wizard(Player):
    def __init__(self, name, power, email):
        Player.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        Player.attack(self)
        print(f'attacking with power {self.power}')


class Archer(Player):
    def __init__(self, name, num_arrows, email):
        Player.__init__(self, email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows {self.num_arrows}')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, email, num_arrows):
        super().__init__(name, power, email)
        Archer.__init__(self, name, num_arrows, email)


# wizard1 = Wizard('Merlin', 40, 'Merlin@gmail.com')
# archer1 = Archer('Robin', 100, 'robin@gmail.com')
# print(wizard1.attack())
# print(archer1.attack())
# # Checking instances
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, Player))
# print(isinstance(wizard1, Archer))
# print(isinstance(wizard1, object))
# wizard1.say()
# archer1.say()

# introspection
# print(dir(wizard1))
hybrid = Hybrid('Erick', 40, 'ermateze@gmail.com', 50)
print(hybrid.email)
print(hybrid.attack())
