import utt_print as p
board_num = 0
boards = {}
p1_p2 = "x"

for index in range(10):
    boards["board" + str(index)] = [" " for space in range(9)]



def main_board():
    return boards["board0"]

def board():
    return boards["board" + str(board_num)]

def tile(tile_index):
    return tile_index-1

def swap_turn(player):
    if player == "x":
        player = "o"
    else:
        player = "x"
    return player

def win_state(current_board):
    for i in [1, 3, 4]:
        for a in range(3):
            if (current_board[a*(3//i)+(a%2)*(i//4)*2] + current_board[a*(3//i)+1*i] + current_board[a*(3//i)+2*i+(a%2)*(i//4)*(-2)]) == (p1_p2 * 3):
                if board_num != 0:
                    main_board()[tile(board_num)] = p1_p2
                return True
    if board().count(" ") == 0:
        if board_num != 0:
            main_board()[tile(board_num)] = "-"
        return "draw"
    return False

def board_state(current_tile):
    if current_tile == " ":
        return p1_p2

def pick_tile(action):
    gap = " "*29
    response = input(f"{gap + action}:\n{gap}     1 2 3\n{gap}     4 5 6\n{gap}     7 8 9\n{gap + " "*7}")
    print('\033c')
    if (response.isdigit()) and (int(response) > 0) and (int(response) < 10):
        if (board_state(board()[tile(int(response))]) == p1_p2):
            p.clear()
            return int(response)
        else:
            p.error_message(p.occupied)
    else:
        p.error_message(p.invalid_input)
    return 0



p.clear()
while win_state(main_board()) == False:
    while board_num == 0:
        p.print_game_state(p1_p2, boards, board_num)
        board_num = pick_tile("Choose a Sector")
    while board_num != 0:
        p.print_game_state(p1_p2, boards, board_num)
        tile_num = pick_tile(" Place a Tile")
        if tile_num != 0:
            board()[tile(tile_num)] = board_state(board()[tile(tile_num)])
            win_state(board())
            board_num = 0
            if win_state(main_board()) == True:
                break
            elif main_board()[tile(tile_num)] == " ":
                board_num = tile_num
            p1_p2 = swap_turn(p1_p2)

p.print_win_state(win_state(board()), p1_p2)
p.print_board(boards, board_num)











# print("""
# \[]\     /[]/
#  \[]\   /[]/
#   \[]\_/[]/
#    []>X<[]
#   /[]/‾\[]\
#  /[]/   \[]\
# /[]/     \[]\
# """)





# print("""


#  _____________
# [=============]
#  ‾‾‾‾‾‾‾‾‾‾‾‾‾


# """)





# print("""
# [I]         [I]
# |H]         [H|
# |H|         |H|
# |H|    _    |H|
# [H]   /^\\   [H]
# \\\\\\_.//^\\\\._///
#  ‾\\\//‾‾‾\\\\//‾
#    ‾‾     ‾‾
# """)





# print("""
# |‾‾‾‾‾‾‾‾‾I=_   
# |HH|‾‾‾‾'=_ ‾|.
# |HH|      |I. ]
# |HH|      [|] | []=‾‾‾= .=‾‾‾=[] [|    |]
# |HH|      |I+ ] []      [|    [] || __ ||
# |HH|____.=‾ _|+ []      [|    [] [|//\\\\|]
# |_________I=‾   []      *=___=[]  []/\\[]
# """)





# print("""
#    \\\\_       _//     [I]         [I]   
#     ‾\\\\_   _//‾      |H]         [H|   ___  
#       ‾\\\\_//‾        |H|         |H|  |[0]| 
#         >X<          |H|    _    |H|   \\=/   []=‾‾‾+. =‾‾‾‾‾=
#       _//‾\\\\_        [H]   /^\\   [H] -.=I=.- []    [] |
#     _//‾   ‾\\\\_      \\\\\\_.//^\\\\._///   [I]   []    []  ‾‾‾‾‾|
#    //‾       ‾\\\\      ‾\\\//‾‾‾\\\\//‾  _=*‾*=_ []    [] =_____=
#                         ‾‾     ‾‾
# """)





# print("""
#     _--=====--_   [O]             _.===========._
#    []‾‾‾‾‾‾‾‾‾[]    )            |_|-=‾‾[I]‾‾=-|_|
#   ||           ||                       |I|
#   ||           ||     =‾‾‾‾‾=           |I|        |     | []=‾‾‾= []=‾‾‾+.
#   ||           ||     |                 |I|        |     | []      []    []
#    []_________[]       ‾‾‾‾‾|          _[I]_       |     | []      []    []
#     ‾--=====--‾       =_____=       |‾*=====*‾|    ‾=___=‾ []      []    []
#                                      ‾‾‾‾‾‾‾‾‾
# """)         





# print("""
#                    | []=============[] | []Current=Board[]
#      x | o | x     | ||  x | o | x  || | ||  x | o | x  || 
#     -----------    | || ----------- || | || ----------- || 
#      o | x | o     | ||  o | x | o  || | ||  o | x | o  || 
#     -----------    | || ----------- || | || ----------- || 
#      x | o | x     | ||  x | o | x  || | ||  x | o | x  || 
#                    | []=============[] | []Current=Board[] 
# -------------------x-------------------x-------------------
#                    |   Current Board   |   \\\\_       _//
#      x | o | x     |     x | o | x     |    ‾\\\\_   _//‾
#     -----------    |    -----------    |      ‾\\\\_//‾
#      o | x | o     |     o | x | o     |        >X<
#     -----------    |    -----------    |      _//‾\\\\_
#      x | o | x     |     x | o | x     |    _//‾   ‾\\\\_
#                    |   Current Board   |   //‾       ‾\\\\ 
# -------------------x-------------------x-------------------
#                    |                   |    _--=====--_
#      x | o | x     |     X | O | X     |   []‾‾‾‾‾‾‾‾‾[]
#     -----------    |    -----------    |  ||           ||
#      o | x | o     |     X | O | X     |  ||           ||
#     -----------    |    -----------    |  ||           ||
#      x | o | x     |     X | O | X     |   []_________[]
#                    |                   |    ‾--=====--‾
# """)