from stat_bar import StatBar, HealthBar, EnergyBar
from enemies import Beastiary
from moves import Moves
from console import clear_console, save_text, text_bank

class Character:
    def __init__(self,
                 name : str,
                 HP : int,
                 ATK : int,
                 DEF : int,
                 LVL : int,
                 ENG : int,
                 ACT : dict):
        self.name = name
        self.MaxHP = HP
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.MaxENG = ENG
        self.ENG = ENG
        self.LVL = LVL
        self.ACT = ACT
        self.ARM = 0
    
    def attack(self, target, move):
        attack_multiplier = Moves[move][1]
        energy_cost = Moves[move][2]
        damage = round(max(max(self.ATK * attack_multiplier - target.DEF, 1) - target.ARM, 0))
        target.HP -= damage
        target.HP = max(target.HP, 0)
        target.ARM = 0
        self.ENG = max(self.ENG - energy_cost, 0)
        target.health_bar.update()
        self.energy_bar.update()
        text = (f"{self.name} dealt {damage} damage to "
              f"{target.name} with {move}")
        save_text(text)
        clear_console()
        for i, text in enumerate(text_bank):
            print(text)
        # print(f"{self.name} dealt {damage} damage to "
        #       f"{target.name} with {move}")
    
    def defend(self, move):
        self.ARM = self.DEF 
        

class Player(Character):
    def __init__(self,
                 name : str,
                 HP : int,
                 ATK : int,
                 DEF : int,
                 LVL : int,
                 ENG : int,
                 ACT : dict):
        super().__init__(name=name, HP=HP, ATK=ATK, DEF=DEF, LVL=LVL, ENG=ENG, ACT=ACT)
        self.stats = StatBar(self)
        self.health_bar = HealthBar(self, colour="green")
        self.energy_bar = EnergyBar(self, colour="yellow")

class Enemy(Character):
    def __init__(self,
                 monster : str):
        name, HP, ATK, DEF, LVL, ENG, ACT = Beastiary[monster]
        super().__init__(name=name, HP=HP, ATK=ATK, DEF=DEF, LVL=LVL, ENG=ENG, ACT=ACT)
        #          mob : str):
        # super().__init__(name=mob[0], HP=mob[1], ATK=mob[2], DEF=mob[3], LVL=mob[4], ENG=mob[5], ACT=mob[6])
        self.stats = StatBar(self)
        self.health_bar = HealthBar(self, colour="red")
        self.energy_bar = EnergyBar(self, colour="yellow")
