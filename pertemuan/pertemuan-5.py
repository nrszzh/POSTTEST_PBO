from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, attack, health, armor):
        self.name = name
        self.attack = attack
        self.health = health
        self.armor = armor

    @abstractmethod
    def ulti(self, target):
        pass #parent nya pass karena wajib diisinya sama subclass

    def hitung_damage(self, target):
        return max(self.attack - target.armor, 0)

    def serang(self, target):
        damage = self.hitung_damage(target)
        target.health -= damage
        print(f'{self.name} meng serang {target.name}. demeg {damage}')

    def __add__(self, healing):
        return self.health + healing

    # def __add__(self, attack):
        # return self.attack + other.attack???

    def __sub__(self, burn):
        darah = self.health
        for i in range(100):
            darah = self.health - burn
            print('darah :', darah)
        self.health = darah
        print(self.health)


class Mage(Hero):
    def hitung_damage(self, target):
        return self.attack #armornya tembuuuusss

    def ulti(self, target):
        return self.attack * 88 - target.health

class Warrior(Hero):
    def hitung_damage(self, target):
        return super().hitung_damage(target) + 10 #bonus 10

    def ulti(self, target):
        return self.attack * 67 - target.health

class Minion():
    def __init__(self, name, health, attack) -> None:
        self.name = name
        self.health = health
        self.attack = attack

    def hitung_damage():
        print('no demeg')

sora = Warrior('Sora', 60, 100, 30)
eudora = Mage('Eudora', 100, 60, 5)
minion = Minion('minion', 50, 3)

# eudora.serang(sora)
# sora.serang(eudora)
# eudora.serang(minion)

# print(sora.ulti(eudora))
# print(eudora + 100)
# print(eudora - 5)

# print(eudora + sora)

print(isinstance(eudora, Hero))  #isistace keluarannya true/false
print(isinstance(eudora, Mage))  #eudora bagian subclas dari mage dan warrior

print(type(eudora))