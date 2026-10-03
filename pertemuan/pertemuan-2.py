# from dataclasses import dataclass, field

# @dataclass
# class Hero:
#     name : str
#     health : float
#     armor : int
#     attack : float

    # def __post_init__(self) -> int:

# -> int: cleancode, tp aslinya cm komen biasa

class Hero:
    jumlahHero = 0

    def __init__(self, name, health, armor, attack):
        self.__name = name 
        self.__health = health
        self.armor = armor
        self.attack = attack

    def __str__(self):  #magic method gda di prak
        return f"attack hero {self.attack}"

    @property
    def getName(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def heroPower(self):
        return self.__health + (self.armor * 1.5)  #getter ga cuma ngeakses, tp bisa kalkulasi

    @health.setter
    def health(self, darahBaru):
        if darahBaru <= 0:
            self.__health = 0
        else:
            self.__health =darahBaru

    @health.deleter
    def health(self):
        health = 0




sniper = Hero('sniper', 100, 4, 15)
print(sniper.armor)

del sniper.health
print(sniper.__dict__)


# print(sniper.name) #bakal error, karna name private
print(sniper.__dict__)
print(sniper._Hero__name)
print(sniper.getName) #karna sdh pakai dekorator dri @property, jdi gapake getName() (tanda kurung)

# print(sniper.health)


