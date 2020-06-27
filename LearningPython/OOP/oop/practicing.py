class Player:
    # Class object attributes
    membership = True

    def __init__(self, name='Anonymus', age=0):
        if Player.membership:
            self.name = name  # Attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def instance(cls, name, age):
        return cls(name, age)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = Player('Erick', 33)
player2 = Player('Roberto', 33)
player1.run('Ho')
player2.run('HI')
# Method without instance only with the class or blueprint.
print(Player.adding_things(3, 5))
player3 = Player.instance('Jesus', 33)
print(Player.adding_things2(3, 5))
print(player3)
