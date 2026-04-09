from map import cave_depth

# Beastiary = {cave_depth[i]: f"enemy {i//2}" for i in range(20)}
# Beastiary = {"cave depth 0": ("Mini Slime", 50, 20, 0, 1, 1, {0: "pounce"}),
            #  "cave depth 1": "enemy1",
            #  "cave depth 2": "enemy1",
            #  "cave depth 3": "enemy1",
            #  "cave depth 4": "enemy1",
            #  "cave depth 5": "enemy1",
            #  "cave depth 6": "enemy1",
            #  "cave depth 7": "enemy1",
            #  "cave depth 8": "enemy1",
            #  "cave depth 9": "enemy1",
            #  "cave depth 10": "enemy1",
            #  "cave depth 11": "enemy1",
            #  "cave depth 12": "enemy1",
            #  "cave depth 13": "enemy1",
            #  "cave depth 14": "enemy1",
            #  "cave depth 15": "enemy1",
            #  "cave depth 16": "enemy1",
            #  "cave depth 17": "enemy1",
            #  "cave depth 18": "enemy1",
            #  "cave depth 19": "enemy1"
            # }

# class Monster:
#     def __init__(self,
#                  name : str,
#                  HP : int,
#                  ATK : int,
#                  DEF : int,
#                  LVL : int,
#                  ENG : int,
#                  ACT : dict):
#         self.name = name
#         self.HP = HP
#         self.ATK = ATK
#         self.DEF = DEF
#         self.ENG = ENG
#         self.LVL = LVL
#         self.ACT = ACT

# # template = Monster(name="",
# #                     HP=0,
# #                     ATK=0,
# #                     DEF=0,
# #                     ENG=0,
# #                     LVL=0,
# #                     ACT={})

# mini_slime = Monster(name="Mini Slime",
#                      HP=50,
#                      ATK=20,
#                      DEF=0,
#                      ENG=1,
#                      LVL=1,
#                      ACT={0: "pounce"})

# scorpion = Monster(name="Scorpion",
#                     HP=75,
#                     ATK=40,
#                     DEF=40,
#                     ENG=4,
#                     LVL=10,
#                     ACT={0: "pinch",
#                          1: "sting"})

# slime = Monster(name="Slime",
#                     HP=75,
#                     ATK=30,
#                     DEF=5,
#                     ENG=1,
#                     LVL=1,
#                     ACT={0: "pounce"})

# Beastiary = {"Mini Slime": mini_slime,
#              "Scorpion": scorpion,
#              "Slime": slime
#              }

#{name: (name, hit points, attack, defence, level, engery, actions)}

Beastiary = {"Mini Slime": ("Mini Slime", 50, 20, 0, 1, 1, {0: "Pounce"}),
             "Scorpion": ("Scorpion", 75, 40, 40, 4, 5, {0: "Pinch",
                                                         1: "Sting"}),
             "Slime": ("Slime", 75, 30, 5, 1, 1, {0: "Pounce"})
             }