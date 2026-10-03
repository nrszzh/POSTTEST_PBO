class Hero:
    def __init__(self, name, health, attack, armor, mana=50):
        self.name = name
        self._health = health
        self.attack = attack
        self.armor = armor
        self.mana = mana

    def diserang(self, jumlah):
        self._health = max(self._health - jumlah, 0)  #biar kalo keserang dia ga mines, tapi 0

    def serang(self, target):
        damage = max(self.attack - target.armor, 0)
        target.diserang(damage)
        print(f'{self.name} menyerang {target.name}, damage {damage}')

        @property
        def health(self):
            return self._health

    def __str__(self): #magic method
        return f'nama hero {self.name}'

class Healing():
    def heal(self, jumlah):
        self._health += jumlah   #self._health = self._health + jumlah (itu mempersingkat)
        print(f'{self.name} melakukan healing sebesar {jumlah}')

class Archer(Hero): #single inherintance
    # pass # mau plek ketiplek atribut hero
    def __init__(self, name, health, attack, armor, mana=50, missChange=50):
        super().__init__(name, health, attack, armor, mana=50) #constructor sama ky superclass supaya mewariskan
        self.missChange = missChange #buat atribut tambahan buat anaknya

    def serang(self, target): # override atau nimpa dari superclass
        super().serang(target) # amati tiru
        print(f'menyerang menggunakan panah')  # modifikasi/ tambahannya
        # print(f'{self.name} menyerang menggunakan panah ke {target.name}')

class EnergyArcher(Archer): #multi level inheritance 
    def __init__(self, name, health, attack, armor, mana=50, missChange=50, energi=100):
        super().__init__(name, health, attack, armor, mana=50, missChange=50) #pke initnya archer
        self.energi = energi

    def serang(self, target):
        if self.energi >= 20:
            self.energi -= 2
            damage = max(self.attack * 2 - target.armor, 0)
            target.diserang(damage)
            print(f'{self.name} menyerang {target.name}. damage {damage}, sisa energi {self.energi}')
        else:
            print('energi habis gada bonus damage')
            super().serang(target)

class Support(Archer, Healing): #multiple inherintace
    pass

class Mage(Hero):
    pass 

roger = Hero('roger', 100, 100, 2, 100)
Widranger = Archer('Widranger', 80, 20, 50, 40)
kimmy = EnergyArcher('Kimmy', 120, 15, 4, 100, 30,)
nana = Support('nana', 100, 15, 4)


roger.serang(Widranger)
Widranger.serang(roger)
nana.serang(kimmy)

nana.heal(100)

for _ in range (8):
    kimmy.serang(roger)

# print(roger.__dict__)
# print(Widranger.__dict__)

# print(roger)
# print(isinstance(Widranger, Archer))
