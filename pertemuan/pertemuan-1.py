import random

class Hero:

    jumlahhero = 1 #atribut class

    def __init__(self, name, health, armor, attack): #constructor 
        self.nama = name     #yg didalam ini atribut instance
        self.health = health
        self.armor = armor
        self.attack = attack
        print('nama saya ridho')
        Hero.jumlahhero += 1

    def serang(self, lawan):
        print(f'{self.name} menyerang {lawan.name}')
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan):
        print(self.name + 'diserang' + lawan.name)
        attack_diterima = attack_lawan
        self.health -= attack_diterima
        print(f'darah {self.name} tersisa {self.health}')

    def healing(self, amount):
        print(self.health)
        self.healh += amount
        print(self.health)


roger = Hero('roger', 100, 4, 15)
sniper = Hero('sniper', 50, 5, 30)

sniper.serang(roger)
roger.diserang(sniper)
sniper.healing(15)











#     #instance method
#     def healthUp(self, up):
#         self.health += up

#     def levelUp(self): #instance karna parameter nya self
#         self.health += 50
#         self.attack += 5
#         self.armor += 2

#     @classmethod
#     def totalHero(cls):
#         print(f'total ')

#     @staticmethod
#     def is_crititcal(peluang):



# roger = Hero('roger', 100, 4, 15)
# print(roger.name)

# sniper = Hero('sniper', 50, 5, 30)


# print(roger__dict__)
