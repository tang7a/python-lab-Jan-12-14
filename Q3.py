class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount


player = GameCharacter("Hero", 100)

player.take_damage(20)
print(player.health)

player.take_damage(80)
print(player.health)

player.heal(20)
print(player.health)