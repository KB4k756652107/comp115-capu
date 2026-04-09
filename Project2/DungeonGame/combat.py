from console import clear_console
from moves import Moves

class Encounter():
    def actions(player):
        move = ""
        for i, move in enumerate(player.ACT.values()):
            effective_range, attack_multiplier, energy_cost = Moves[move]
            print(f"[{move}|[{i}]]", end=" ")
        print("")
        response = input("Enter a move number: ")
        while response.isnumeric() is False or (int(response) + 1) > len(player.ACT):
            response = input("Enter a move number: ")
        response = int(response)
        move = player.ACT[response]
        print(f"{move}:\n"
              f"     Range:                 {Moves[player.ACT[response]][0]}\n"
              f"     Attack Multiplier:     {Moves[player.ACT[response]][1]}\n"
              f"     Energy Cost:           {Moves[player.ACT[response]][2]}")
        input("Press [ENTER] to continue -->")
        clear_console()
        return move
            #  | {effective_range}:{attack_multiplier}:{energy_cost} 
    # def option_attack(player):
    #     for move in Player.ACT.values():
    #         print(f"[{}]")
    def option_defend():
        pass
    def option_movement():
        pass
    def items():
        pass