# #Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
    print ('-'*13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ('-'*13)

def XO_place(player):
    valid = False
    while not valid:
        answer = int(input("В какую ячейку поставить крестик или нолик: "))
        if answer >= 1 and answer <= 9:
            if (str(board[answer-1]) not in "XO"):
                board[answer-1] = player
                valid = True
            else:
                print ("Эта ячейка уже занята, введите другое число.")
        else:
            print ("Ошибка! Введите число от 1 до 9.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def play(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            XO_place("X")
        else:
            XO_place("O")
        count += 1
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграли")
                win = True
                break
        if count == 9:
            print ("Ничья.")
            break
    draw_board(board)

play(board)