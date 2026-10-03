class Shop:
    def __init__(self, nama):
        self.nama = nama

def proses_pembelian(self, hero, item):
        if hero.gold >= item.harga:
            hero.gold -= item.harga
            print(f"[{self.nama}] {hero.nama} membeli {item.nama} "
                f"({item.harga} gold), sisa gold {hero.gold}")
            return True
        print(f"[{self.nama}] Gold {hero.nama} tidak cukup untuk {item.nama}")
        return False

class Item:
    def __init__(self, nama, harga, bonus_attack=0, bonus_armor=0):
        self.nama = nama
        self.harga = harga
        self.bonus_attack = bonus_attack
        self.bonus_armor = bonus_armor

    def __str__(self):
        return(f"Item: {self.nama}  | +{self.bonus_attack} attack  |  +{self.bonus_armor} armor")

class Skill:
    def __init__(self, nama, damage, mana_cost):
        self.nama = nama
        self.damage = damage
        self.mana_cost = mana_cost

    def __str__(self):
        return f"{self.nama} {self.damage} damage, {self.mana_cost} mana"


class Hero:
    jumlahHero = 0
    MAX_SLOT = 4

    def __init__(self, nama, health, mana, armor, attack, gold, list_skill):
        self.nama = nama
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.gold = gold
        self.list_skill = list_skill
        self._inventory = [] #agregasi
        #komposisi
        self._skill = [Skill(nama, dmg, mana) for nama, dmg, mana in list_skill] 
        

    #penggunaan asosiasi
    def beli_item(self, shop, item):
        if len(self._inventory) >= Hero.MAX_SLOT:
            print(f"Inventory {self.nama} dah penuh brek")
            return
        if shop.proses_pembelian(self, item):
            self._inventory.append(item)

    #agregasi
    def ambil_item(self, item):
        if len(self._inventory) < Hero.MAX_SLOT:
            self._inventory.append(item)
            print(f"+ {self.nama} mengambil {item.nama}")

    def cast_skill(self, nomor_skill, lawan):
        skill = self.skills[nomor_skill - 1]
        if self.mana < self.mana_cost:
            print(f"Mana {self.name}, tidak cukup untuk {skill.name}")
            return
        self.mana -= skill.mana_cost
        lawan.health -= skill.damage
        print(f"{self.name}, memakai {skill.name} ke {lawan.name}, sisa health {lawan.name}: {lawan.health}")


brodi = Hero(nama="Brodi", health=3000, mana=1000, armor=10, attack=1000, gold=4000, list_skill=(("tembak", 100, 10), ("loncat", 10, 1)))
estes = Hero(nama="Estes", health=3000, mana=1000, armor=10, attack=1000, gold=4000, list_skill=(("tembak", 100, 10), ("loncat", 10, 1)))
shop = Shop("Belanja Item")
bod = Hero("BOD", 3100, bonus_attack=160)
winter = Item("Winter", 2140, bonus_attack=15, bonus_armor=45)

brodi.cast_skill(1, skills)
estes.cast_skill()

brodi.beli_item(shop, bod)
brodi.ambil_item(bod)
print()