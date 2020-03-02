
# Tic Tac Toe: Human vs Human

# Didn't get this on my own - Create a 3 x 3 board: where each box is numbered from 1 to 3
#
# Done on my own - Code the winning condition: that is if boxes [1,2,3] all have only X or only O then the respective player wins
#
# Done on my own - If there is no winning condition then it's a draw
#
# Done on my own - Put all the above in a while true loop, at the end of each game ask the player if you wanna continue and if no then False.


# Looking over this skeleton, I notice that it is made up of about 6 main components:
#
# new_board - done, same as render
# render - done
# get_move - done
# make_move - done, same as get_move
# get_winner - done
# is_board_full - done


# works correctly
def render(board):
    # Each element in our list-of-lists will represent a square on the board. In each sqaure we will need to be able to represent
    # the 3 possible states - O, X and empty.

    # zero, one, two, three, four, five, six, seven, eight = " ", " ", " ", " ", " ", " ", " ", " ", " "
    # zero, one, two, three, four, five, six, seven, eight = None, None, None, None, None, None, None, None, None

    # two = "x"
    # board = [[zero, one, two], [three, four, five], [six, seven, eight]]
    # print(board)
    #
    # print("-----------------")
    # print("||"+" "+str(zero)+" "+"||"+" "+str(one)+" "+"||"+" "+str(two)+" "+"||")
    # print("-----------------")
    # print("||"+" "+str(three)+" "+"||"+" "+str(four)+" "+"||"+" "+str(five)+" "+"||")
    # print("-----------------")
    # print("||"+" "+str(six)+" "+"||"+" "+str(seven)+" "+"||"+" "+str(eight)+" "+"||")
    # print("-----------------")

    # print("\n")
    print("-----------------")
    print("||"+" "+str(board[0][0])+" "+"||"+" "+str(board[0][1])+" "+"||"+" "+str(board[0][2])+" "+"||")
    print("-----------------")
    print("||"+" "+str(board[1][0])+" "+"||"+" "+str(board[1][1])+" "+"||"+" "+str(board[1][2])+" "+"||")
    print("-----------------")
    print("||"+" "+str(board[2][0])+" "+"||"+" "+str(board[2][1])+" "+"||"+" "+str(board[2][2])+" "+"||")
    print("-----------------")
    print("\n")


# works correctly
def get_winner(board):

    w = 0

    # return winner if
    p1 = [board[0][0], board[1][0], board[2][0]]
    p2 = [board[2][0], board[2][1], board[2][2]]
    p3 = [board[0][2], board[1][2], board[2][2]]
    p4 = [board[0][0], board[0][1], board[0][2]]
    p5 = [board[0][1], board[1][1], board[2][1]]
    p6 = [board[1][0], board[1][1], board[1][2]]
    p7 = [board[0][0], board[1][1], board[2][2]]
    p8 = [board[0][2], board[1][1], board[2][0]]

    if(p1.count("x")==3 or p2.count("x")==3 or p3.count("x")==3 or p4.count("x")==3 or p5.count("x")==3 or p6.count("x")==3 or p7.count("x")==3 or p8.count("x")==3):
        print("DEATH: Did you enjoy your reprieve?")
        print("KNIGHT: Yes, I did.")
        print("DEATH: Your time is up. Nothing escapes me. No one escapes me.")
        print("Over there against the dark, stormy sky. They are all there. The smith and Lisa and the knight and Raval and Jöns and Skat. And Death, the severe master, invites them to dance. He tells them to hold each other's hands and then they must tread the dance in a long row. And first goes the master with his scythe and hourglass, but Skat dangles at the end with his lyre. They dance away from the dawn and it's a solemn dance towards the dark lands, while the rain washes their faces and cleans the salt of the tears from their cheeks.\n")
        w = 1
        return "win"

    if(p1.count("o")==3 or p2.count("o")==3 or p3.count("o")==3 or p4.count("o")==3 or p5.count("o")==3 or p6.count("o")==3 or p7.count("o")==3 or p8.count("o")==3):
        print("DEATH: We will meet again very soon. Till then enjoy your reprieve.\n")
        w = 1
        return "win"

    # check board full
    full_status = is_board_full(board)

    # return draw if - no winner and board full
    if(w == 0 and full_status==True):
        print("DEATH: We will continue our game later. (It's a draw)")
        return "draw"

    # return ongoing if: no winner and board not full
    if(w == 0 and full_status==False):
        return "ongoing"


# works correctly
def is_board_full(board):
    e = board[0].count(" ") + board[1].count(" ") + board[2].count(" ")

    if(e != 0):
        return False

    if(e == 0):
        return True



# works correctly
def game(board, status):

    # do something about status, what if the game is ongoing

    # the followng lines are executed at the start of each new game
    print("\nDEATH: I am Death. I have been walking by your side for a long time. Are you prepared?")
    print("KNIGHT: My body is frightened, but I am not.")
    print("DEATH: Well, there is no shame in that.")
    print("KNIGHT: Wait a moment.")
    print("DEATH: That's what they all say. I grant no reprieves.")
    print("KNIGHT: You play tic-tac-toe, don't you?")
    print("DEATH: Yes, in fact I'm quite a good tic-tac-toe player.")
    print("DEATH: Why do you want to play tic-tac-toe with me?")
    print("KNIGHT: The condition is that I may live as long as I hold out against you. If I win, you will release me. Is it agreed?")
    print("The KNIGHT holds out his two fists to DEATH, who smiles at him suddenly. DEATH points to one of the KNIGHT'S hands; it contains X.")
    print("KNIGHT: You drew X!")
    print("DEATH: Very appropriate. Don't you think so?")
    print("The KNIGHT and DEATH bend over the tic-tac-toe board.")

    render(board)
    turn = 0
    flag = True

    # for every odd turn X will play and for every even turn O will play

    while(flag):

        turn = turn + 1

        board = get_move(turn, board)
        # board = [[zero, "x", two], [three, four, five], [six, seven, eight]]
        render(board)

        # because 5 turns minimum are required for X to get the winning condition
        if(turn >= 5):
            status = get_winner(board)


        if status == "win" or "draw":
            flag = False
        if status == "ongoing":
            flag = True


# works correctly
def get_move(turn, board):

    if turn%2!=0: #if odd, 1,3,5,7,9
        i, j = map(int, input("DEATH plays: ").split())
        board[i][j] = "x"
        if(turn == 1):
            print("DEATH: Let us begin.")
        elif(turn == 3):
            # print("DEATH: And yet you don't want to die.")
            print("DEATH: What are you waiting for?")
            print("KNIGHT: I want knowledge! Not faith, not assumptions, but knowledge. I want God to stretch out His hand, uncover His face and speak to me.")
            print("DEATH: But He remains silent.")
        elif(turn == 5):
            print("DEATH: Most people think neither of death nor nothingness.")
            print("KNIGHT: But one day you stand at the edge of life and face darkness.")
            print("DEATH: That day.")

    else: #if even, 2,4,6,8,10
        i, j = map(int, input("KNIGHT plays: ").split())
        board[i][j] = "o"
        if(turn == 2):
            print("KNIGHT: Through my indifference to my fellow men, I have isolated myself from their company. Now I live in a world of phantoms. I am imprisoned in my dreams and fantasies.")
            print("DEATH: And yet you don't want to die.")
            print("KNIGHT: Yes, I do.")
        elif(turn == 4):
            print("KNIGHT: I call out to Him in the darkness. But it's as if no one was there.")
            print("DEATH: Perhaps there isn't anyone.")
            print("KNIGHT: Then life is a preposterous horror. No man can live faced with Death, knowing everything's nothingness.")
        elif(turn == 6):
            print("KNIGHT: I understand what you mean.")

    return board



# works correctly
def starter():

    # zero, one, two, three, four, five, six, seven, eight = " ", " ", " ", " ", " ", " ", " ", " ", " "
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    status = "ongoing"

    stat = game(board, status)

    if stat == "win" or "draw":
        c = input("Do you wanna continue this ordeal?: y or n: ")

        if c == "n":
            print("GoodBye!")
            return

        if c == "y":
            starter()



starter()
