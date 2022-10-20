class Player:
    def __init__(self, name):
        self.name = name

class Computer:
    def __init__(self):
        super().__init__("NPC")

    def respond(self, player):
        print("Hello", player.name, "I am ", self.name)

class User(Player):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def greet(self):
        print("Hi! what is your name?")

computer = Computer()
user = User("User", 1)
user.greet()
computer.respond(user)
