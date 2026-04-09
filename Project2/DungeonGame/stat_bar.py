import os

os.system("")

class StatBar:
    symbol_remaining : str = "█"
    symbol_lost : str = "_"
    barrier : str = "|"
    colours : dict = {"red": "\033[91m",
                     "purple": "\33[95m",
                     "blue": "\33[34m",
                     "blue2": "\33[36m",
                     "blue3": "\33[96m",
                     "green": "\033[92m",
                     "green2": "\033[32m",
                     "brown": "\33[33m",
                     "yellow": "\33[93m",
                     "grey": "\33[37m",
                     "default": "\033[0m"
                     }

    def __init__(self,
                 entity,
                 length : int = 50,
                 is_coloured : bool = True,
                 colour : str = ""):
        self.entity = entity
        self.length = length

        self.is_coloured = is_coloured
        self.colour = self.colours.get(colour) or self.colours["default"]
    
    def stats(self):
        print(f"{self.entity.name}'s HP: {self.entity.HP}/{self.entity.MaxHP}"
              f" | ENG: {self.entity.ENG}/{self.entity.MaxENG}"
              f" | ATK: {self.entity.ATK} | DEF: {self.entity.DEF}")

    # def draw(self):
    #     remaining_bars = round(self.current_value / self.max_value * self.length)
    #     lost_bars = self.length - remaining_bars
    #     print(f"{self.barrier}"
    #           f"{self.colour if self.is_coloured else ""}"
    #           f"{remaining_bars * self.symbol_remaining}"
    #           f"{lost_bars * self.symbol_lost}"
    #           f"{self.colours["default"] if self.is_coloured else ""}"
    #           f"{self.barrier}")

class HealthBar(StatBar):
    def __init__(self,
                 entity,
                 length : int = 50,
                 is_coloured : bool = True,
                 colour : str = ""):
        super().__init__(entity=entity, length=length, is_coloured=is_coloured, colour=colour)
        self.max_value = entity.MaxHP
        self.current_value = entity.HP
    
    def update(self):
        self.current_value = self.entity.HP
    
    def draw(self):
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.barrier}"
              f"{self.colour if self.is_coloured else ""}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colours["default"] if self.is_coloured else ""}"
              f"{self.barrier}")

class EnergyBar(StatBar):
    def __init__(self,
                 entity,
                 length : int = 50,
                 is_coloured : bool = True,
                 colour : str = ""):
        super().__init__(entity=entity, length=length, is_coloured=is_coloured, colour=colour)
        self.max_value = entity.MaxENG
        self.current_value = entity.ENG
    
    def update(self):
        self.current_value = self.entity.ENG
    
    def draw(self):
        bar_length = max(round((self.length) / self.max_value - 0.5) - 1, 0)
        remainder = self.length - bar_length * self.max_value
        lost_bars = self.max_value - self.current_value
        print(f"{self.barrier}"
              f"{self.colour if self.is_coloured else ""}", end="")
        for _ in range(self.current_value):
            spread = remainder // self.max_value
            print(f"{bar_length * self.symbol_remaining}"
                  f"{spread * self.symbol_remaining}"
                  f"{self.barrier}", end="")
            remainder -= spread
        for _ in range(lost_bars):
            spread = remainder // self.max_value
            print(f"{bar_length * self.symbol_lost}"
                  f"{spread * self.symbol_lost}"
                  f"{self.barrier}", end="")
            remainder -= spread
        print("\b", end="")
        print(f"{self.colours["default"] if self.is_coloured else ""}"
              f"{self.barrier}")

#Don't forget about EnergyBar overflowing