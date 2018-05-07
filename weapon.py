class Weapon:
    def __init__(self, name, damage=20):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return self.name
