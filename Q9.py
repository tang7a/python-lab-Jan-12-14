class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        if other.health < 0:
            other.health = 0

    def is_alive(self):
        return self.health > 0


c1 = Character("Knight", 50, 10)
c2 = Character("Orc", 40, 8)

while c1.is_alive() and c2.is_alive():
    c1.attack(c2)
    if not c2.is_alive():
        break
    c2.attack(c1)

print("Game over")