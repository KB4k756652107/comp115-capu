import camp as CAM
from character import Player, Enemy
import combat as COM
import enemies as E
import items as I
import map as M
import console as CON

player = Player("player", 100, 30, 10, 1, 3, {0: "Lunge",
                                              1: "Punch",
                                              2: "Kick"})
enemy = Enemy("Slime")
# enemy = CHA.Enemy(E.beastiary["Scorpion"])
# enemy = CHA.Enemy(E.beastiary["cave depth 0"])
# enemy = CHA.Enemy("slime", 5, 1, 0, 1, {0: "pounce"})
# player.ACT[0] = "punch"

def main():
    # print(M.cave_depth)
    # for i in M.cave_depth.values():
    #     print(i)
    # for e in E.beastiary.values():
    #     print(e)
    while 1:
        # player.stats.stats()
        # player.health_bar.draw()
        # player.energy_bar.draw()
        # enemy.stats.stats()
        # enemy.health_bar.draw()
        # enemy.energy_bar.draw()

        
        if (player.HP == 0) or (enemy.HP == 0):
            break
        else:
            player.ENG = player.MaxENG
            CON.clear_console()
        while player.ENG > 0:
            player.stats.stats()
            player.health_bar.draw()
            player.energy_bar.draw()
            enemy.stats.stats()
            enemy.health_bar.draw()
            enemy.energy_bar.draw()

            if (player.HP == 0) or (enemy.HP == 0):
                break

            player.attack(enemy, COM.Encounter.actions(player))
        CON.save_text("", True)
        enemy.attack(player, enemy.ACT[0])
        # enemy.attack(player, enemy.ACT[1])
    player.stats.stats()
    player.health_bar.draw()
    player.energy_bar.draw()
    enemy.stats.stats()
    enemy.health_bar.draw()
    enemy.energy_bar.draw()
        

if __name__ == '__main__':
    main()