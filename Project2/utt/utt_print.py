invalid_input = "Only Numbers Between 1-9"
occupied = "This Tile is Occupied"
text_index = {
    "x" : 0,
    "o" : 7,
    "-" : 14,
    "turn" : 21,
    "win" : 29,
    "draw" : 37,
    "border" : 44
}

with open(r"utt_file.txt", 'r' , encoding='utf-8-sig') as f:
    start = 0
    end = 0
    segments = []
    for i in range(45):
        line = f.readline().rstrip()
        if len(line) < 15:
            line = (line + " "*(15 - len(line)))
        segments.append(line)


def clear():
    print('\033c\n', flush=True)

def error_message(message = " "):
    clear()
    print(message, flush=True)

def print_turn(player):
    index_p = text_index[player]
    index_t = text_index["turn"]
    for i in range(7):
        print(segments[index_p+i] + segments[index_t+i])
    print(" "*15 + segments[index_t+7], flush=True)

def print_board(game_board, current_board_num):
    sub_row = 0
    board_line = ""
    line_seg = ""
    gap = " "*7

    def main_board():
        return game_board["board0"]
    
    def board(board_num):
        return game_board["board" + str(board_num)]
    
    def sub_board_line(board_num, y):
        text = ""
        if y%2 == 1:
            for i in range(3):
                text = text + " " + board(board_num)[sub_row+i] + " "
                if i//2 != 1:
                    text = text + "|"
        else:
            text = "-----------"
        return text
    
    def add_space(text):
        space_num = int((19 - len(text))/2)
        return " "*space_num


    for row in range (0, 9, 3):
        board_row = [main_board()[row+x] for x in range(3)]
        for a in range(7):
            for b in range(3):
                if board_row[b] != " ":
                    line_seg = segments[text_index[board_row[b]] + a]
                elif (("board" + str(current_board_num)) == ("board" + str(row+b+1))) or (current_board_num == 0):
                    if (a == 0) or (a == 6):
                        line_seg = "[]=============[]"
                    else:
                        line_seg = sub_board_line(row+b+1, a)
                        line_seg = "||" + line_seg + "||"
                elif (a == 0) or (a == 6):
                    line_seg = " "
                else:
                    line_seg = sub_board_line(row+b+1, a)
                line_seg = add_space(line_seg) + line_seg + add_space(line_seg)
                board_line = board_line + line_seg
                if b//2 != 1:
                    board_line = board_line + "|"
            print(gap + board_line, flush=True)
            board_line = ""
            if a%2 == 1:
                sub_row += 3
        if row != 6:
            print(gap + segments[text_index["border"]], flush=True)
        sub_row = 0

def print_game_state(player, game_board, current_board):
    print_turn(player)
    print_board(game_board, current_board)

def print_win_state(win_state, player):
    if win_state == True:
        index_p = text_index[player]
        index_w = text_index["win"]
        gap = " "*6
        for i in range(7):
            print(gap + segments[index_p+i] + segments[index_w+i])
        print(gap + " "*15 + segments[index_w+7], flush=True)
    else:
        index_d = text_index["draw"]
        gap = " "*14
        for i in range(7):
            print(gap + segments[index_d+i], flush=True)
        print('\n', flush=True)