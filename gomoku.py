"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""

def is_empty(board):
    for i in range(7):
        for j in range(7):
            if board[i][j] == "b":
                return False
            if board[i][j] == "w":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    #8x8 board
    #0,1 Left to right
    #1,0 top to bottom
    #1,1 up left to low right
    #1,-1 up right to low left
    right_open = False
    left_open = False
    top_open = False
    bottom_open = False
    top_left_open = False
    bottom_right_open = False
    top_right_open = False
    bottom_left_open = False
    if length == 8:
        return "CLOSED"
    if d_y == 0 and d_x == 1: #LTR
        if x_end != 0 and x_end !=7:
            if x_end +1 == length:
                left_open = False
            elif board[y_end][x_end-1-length] == " ":
                left_open = True
            if board[y_end][x_end + 1] == " ":
                right_open = True
            if right_open != left_open:
                return "SEMIOPEN"
            if right_open and left_open:
                return "OPEN"
            else:
                return "CLOSED"
        if x_end == 7:
            if board[y_end][x_end - length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    #"====================================================================="
    if d_y == 1 and d_x == 1: #ENDS AT BOTTOM RIGHT CORNER
        if y_end == 7 and x_end - length +1== 0:
            return "CLOSED"
        if x_end == 7 and y_end - length +1== 0:
            return "CLOSED"
        if y_end == 7:
            if board[y_end - length][x_end-length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if x_end == length-1:
            if board[y_end +1][x_end+1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if y_end == length-1:
            if board[y_end +1][x_end+1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if x_end == 7:
            if board[y_end - length][x_end-length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"    
        if board[y_end-length][x_end - length] == " ":
                top_left_open = True
        if board[y_end+1][x_end + 1] == " ":
            bottom_right_open = True
        if bottom_right_open != top_left_open:
            return "SEMIOPEN"
        if bottom_right_open and top_left_open:
            return "OPEN"
        else:
            return "CLOSED"
    #"======================================================================================="
    if d_y == 1 and d_x == 0: #ENDS AT BOTTOM
        
        if y_end !=7:
            if y_end +1 == length:
                top_open = False
            elif board[y_end-length-1][x_end] == " ":
                top_open = True
            if board[y_end+1][x_end] == " ":
                bottom_open = True
            if top_open != bottom_open:
                return "SEMIOPEN"
            if top_open and bottom_open:
                return "OPEN"
            else:
                return "CLOSED"
        if y_end == 7:
            if board[y_end-length][x_end] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    #"====================================================================="
    if d_y == 1 and d_x == -1: #ends at BOTTOM LEFT CORNER
#             x = 7; y = 0; d_x = -1; d_y = 1; length = 7
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#    # put_seq_on_board(board, 2, 3, d_y, d_x, 1, "b")

#     print_board(board)
    
#     y_end = 6
#     x_end = 1
        if x_end == 0 and y_end - length +1== 0:
            return "CLOSED"
        if y_end == 7 and x_end == 7:
            return "CLOSED"
        if x_end == 0:
            if board[y_end - length][length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if y_end == 7:
            if board[y_end - length][x_end + length] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if y_end - length +1== 0:
            if board[y_end + 1][x_end -1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if board[y_end-length][x_end + length] == " ":
            top_right_open = True
        if board[y_end+1][x_end - 1] == " ":
            bottom_left_open = True
        if bottom_left_open != top_right_open:
            return "SEMIOPEN"
        if bottom_left_open and top_right_open:
            return "OPEN"
        else:
            return "CLOSED"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    #8x8 board
    #0,1 Left to right
    #1,0 top to bottom
    #1,1 up left to low right
    #1,-1 up right to low left
    if col == "b":
        othercol = "w"
    if col == "w":
        othercol = "b"

    if d_y == 0 and d_x == 1: #LTR
        count = 1
        count2 = 0
        #x start = 0
        for i in range(8): 
            if board[i][x_start] == col: #x start should stay constant, 
                count2 += 1
                if i == 0:
                    j = 0
                    while j != 7 and board[j+1][x_start] == col:
                        j += 1
                        count +=1
                    if count == length and count != 8 and board[count][x_start] == " ":
                        semi_open_seq_count += 1
                        count = 1
                    else:
                        count = 1
                elif i != 7 and board[i-1][x_start] != col:
                    k = i
                    while k != 7 and board[k+1][x_start] == col:
                        k += 1
                        count += 1
                    if count == length and i+count == 8: #only way i+count == 8 if its semi open at the end of the board. can i+count ever be >8? idts but CHECKKKKKK
                        semi_open_seq_count += 1
                        count = 1
                    elif count == length and board[i+count][x_start] == " " and board[i-1][x_start] == " ":
                        open_seq_count += 1
                        count = 1
                    elif count == length and board[i+count][x_start] != " " and board[i-1][x_start] == " ":
                        semi_open_seq_count += 1
                        count = 1
                    elif count == length and board[i+count][x_start] == " " and board[i-1][x_start] != " ":
                        semi_open_seq_count += 1
                        count = 1 

    #"======================================================================================="
    if d_y == 1 and d_x == -1: #STARTS AT TOP RIGHT
        count = 1
        #x start = 7 or y start = 0

        if y_start == 0 and x_start == 1:
            open_seq_count = 0
            semi_open_seq_count = 0
        elif x_start == 7 and y_start == 6:
                open_seq_count = 0
                semi_open_seq_count = 0
        elif x_start == 7: #on RIGHTmost column
            temp = 7-y_start+1
            for i in range(7-y_start+1): 
                if board[y_start+i][x_start-i] == col: #x start going up, y start is literally going up, decreasing
                   # count += 1
                    if i == 0:
                        j = 0
                        while j != 7 and board[j+1][j-1] == col:
                            j += 1
                            count +=1
                        if count == length and count <=temp and board[y_start +count][x_start-count] == " ":
                            semi_open_seq_count += 1
                            count = 1
                        else:
                            count = 1
                    elif i+y_start <7 and board[i-1][i+1] != col:
                        k = i
                        while k != 7 and board[k+1][k-1] == col:
                            k += 1
                            count += 1
                        if count == length and i+count == 7-y_start: #only way i+count == 8 if its semi open at the end of the board. can i+count ever be >8? idts but CHECKKKKKK
                            semi_open_seq_count += 1
                            count = 1
                        elif count == length and board[i+count][i-count] == " " and board[i-1][i+1] == " ":
                            open_seq_count += 1
                            count = 1
                        elif count == length and board[i+count][i-count] != " " and board[i-1][i+1] == " ":
                            semi_open_seq_count += 1
                            count = 1
                        elif count == length and board[i+count][i-count] == " " and board[i-1][i+1] != " ":
                            semi_open_seq_count += 1
                            count = 1 
        elif y_start == 0: #on RIGHTmost column
            temp = 7-y_start+1
            for i in range(7-y_start+1): 
                if board[y_start+i][x_start-i] == col: #x start going up, y start is literally going up, decreasing
                   # count += 1
                    if i == 0:
                        j = 0
                        while j != 7 and board[j+1][j-1] == col:
                            j += 1
                            count +=1
                        if count == length and count <=temp and board[y_start +count][x_start-count] == " ":
                            semi_open_seq_count += 1
                            count = 1
                        else:
                            count = 1
                    elif i+y_start <7 and board[i-1][i+1] != col:
                        k = i
                        while k != 7 and board[k+1][k-1] == col:
                            k += 1
                            count += 1
                        if count == length and i+count == 7-y_start: #only way i+count == 8 if its semi open at the end of the board. can i+count ever be >8? idts but CHECKKKKKK
                            semi_open_seq_count += 1
                            count = 1
                        elif count == length and board[i+count][i-count] == " " and board[i-1][i+1] == " ":
                            open_seq_count += 1
                            count = 1
                        elif count == length and board[i+count][i-count] != " " and board[i-1][i+1] == " ":
                            semi_open_seq_count += 1
                            count = 1
                        elif count == length and board[i+count][i-count] == " " and board[i-1][i+1] != " ":
                            semi_open_seq_count += 1
                            count = 1 
    #"====================================================================="
    if d_y == 1 and d_x == -1: #URTLL
        count = 0
        if y_start != 0 and x_start != 7:
            for i in range(8):
                if x_start >= i and board[y_start+i][x_start-i] == col:
                    count += 1
                if x_start >= i and board[y_start+i][x_start-i] != col:
                    count = 0
                if count == length:
                    if i == 7 or board[y_start+i][x_start-i] == othercol:
                        semi_open_seq_count += 1
                    elif board[y_start+i+1][x_start-i-1] == "" and board[y_start-1][x_start + 1] == "":
                        open_seq_count += 1
        if y_start == 0 and x_start == 7:
            for i in range(8):
                if board[y_start+i][x_start-i] == col:
                    count += 1
                if board[y_start+i][x_start-i] != col:
                    count = 0
                if count == length:
                    if board[y_start+i+1][x_start-i-1] == "" and board[y_start-1][x_start +1]  == "":
                        open_seq_count += 1
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):

    #def detect_row(board, col, y_start, x_start, length, d_y, d_x)
    open_seq_count, semi_open_seq_count = 0, 0
    search_range = 9-length

    vert_rows = []
    hor_rows= []
    ultbr_rows = []
    urtbl_rows = []
    for i in range(search_range): #say length 5, goes 0,1,2,3
        for j in range(7): #goes 0,1,2,3,4,5,6,7
            placeholder1 = detect_row(board, col, i, j, length, 1, 0)
            # looks for vert rows 
            vert_rows.append(placeholder1)
            placeholder2 = detect_row(board, col, j, i, length, 0, 1)
            hor_rows.append(placeholder2)
    
    for i in range(search_range):
        for j in range(search_range):
            #say length 7, goes 0,1
            ultbr_rows.append(detect_row(board, col, i, j, length, 1, 1))
    
    for i in range(search_range):
        for j in range(7,length,-1):
            #say length 5, y needs to go 0,1,2,3, x needs to go 7,6,5,4
            urtbl_rows.append(detect_row(board, col, i, j, length, 1, -1))
    #inefficient but ehhhhh
    for i in range(len(vert_rows)):
        open_seq_count += vert_rows[i][0] 
        semi_open_seq_count += vert_rows[i][1]
    for i in range(len(hor_rows)):
        open_seq_count += hor_rows[i][0]
        semi_open_seq_count += hor_rows[i][1]
    for i in range(len(urtbl_rows)):
        open_seq_count += urtbl_rows[i][0]
        semi_open_seq_count += urtbl_rows[i][1]
    for i in range(len(ultbr_rows)):
        open_seq_count += ultbr_rows[i][0]
        semi_open_seq_count += ultbr_rows[i][1]

    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    temp_high_score = 0
    acc_high_xcoord = 0
    acc_high_ycoord = 0
    acc_highscore = 0
    tempboard = board
    for i in range(8):
        for j in range(8):
            if tempboard[i][j] == " ":
                tempboard[i][j] == "b"
                temp_high_score = score(tempboard)
                if temp_high_score > acc_highscore:
                    acc_high_xcoord = j
                    acc_high_ycoord = i
                    temp_high_score = acc_highscore
    move_y = acc_high_ycoord
    move_x = acc_high_xcoord
            
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    count = 0
    for i in range(7):
        for j in range(7):
            if board[i][j] == " ":
                count += 1
    if count == 0:
        return "Draw"
    placeholder = detect_rows(board, "w", 5)
    if placeholder[0] >0 or (placeholder[1]>0):
        return "White won"
    placeholder = detect_rows(board, "b", 5)
    if (placeholder[0] >0) or (placeholder[1]>0):
        return "Black won"
    else:
        return "Continue playing"



def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


# def test_is_empty():
#     board  = make_empty_board(8)
#     if is_empty(board):
#         print("TEST CASE for is_empty PASSED")
#     else:
#         print("TEST CASE for is_empty FAILED")

# def test_is_bounded():
#     board = make_empty_board(8)
#     x = 6; y = 1; d_x = -1; d_y = 1; length = 5
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#    # put_seq_on_board(board, 2, 3, d_y, d_x, 1, "b")

#     print_board(board)

#     y_end = 5
#     x_end = 2
#     print(is_bounded(board, y_end, x_end, length, d_y, d_x))

# def test_detect_row():
#     board = make_empty_board(8)
#     x = 0; y = 0; d_x = 1; d_y = 0; length = 2
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     #put_seq_on_board(board, y, 1, d_y, d_x, 2, "w")

#     put_seq_on_board(board, 0,4, d_y, d_x, 2, "w")
#    # put_seq_on_board(board, 0,3, d_y, d_x, 1, "b")


#     print_board(board)
#     print(detect_row(board, "w", y, x, length, d_y, d_x))

# def test_detect_rows():
#     board = make_empty_board(8)
#     x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     print_board(board)
#     if detect_rows(board, col,length) == (1,0):
#         print("TEST CASE for detect_rows PASSED")
#     else:
#         print("TEST CASE for detect_rows FAILED")

# def test_search_max():
#     board = make_empty_board(8)
#     x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
#     put_seq_on_board(board, y, x, d_y, d_x, length, col)
#     x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
#     put_seq_on_board(board, y, x, d_y, d_x, length, col)
#     print_board(board)
#     if search_max(board) == (4,6):
#         print("TEST CASE for search_max PASSED")
#     else:
#         print("TEST CASE for search_max FAILED")

# def easy_testset_for_main_functions():
#     # print(test_is_empty())
#     print(test_is_bounded())
#     #print(test_detect_row())
#    # print(test_detect_rows())
#     #print(test_search_max())

# def some_tests():
#     board = make_empty_board(8)

#     board[0][5] = "w"
#     board[0][6] = "b"
#     y = 5; x = 2; d_x = 0; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     print_board(board)
#     analysis(board)
    
#     # Expected output:
#     #       *0|1|2|3|4|5|6|7*
#     #       0 | | | | |w|b| *
#     #       1 | | | | | | | *
#     #       2 | | | | | | | *
#     #       3 | | | | | | | *
#     #       4 | | | | | | | *
#     #       5 | |w| | | | | *
#     #       6 | |w| | | | | *
#     #       7 | |w| | | | | *
#     #       *****************
#     #       Black stones:
#     #       Open rows of length 2: 0
#     #       Semi-open rows of length 2: 0
#     #       Open rows of length 3: 0
#     #       Semi-open rows of length 3: 0
#     #       Open rows of length 4: 0
#     #       Semi-open rows of length 4: 0
#     #       Open rows of length 5: 0
#     #       Semi-open rows of length 5: 0
#     #       White stones:
#     #       Open rows of length 2: 0
#     #       Semi-open rows of length 2: 0
#     #       Open rows of length 3: 0
#     #       Semi-open rows of length 3: 1
#     #       Open rows of length 4: 0
#     #       Semi-open rows of length 4: 0
#     #       Open rows of length 5: 0
#     #       Semi-open rows of length 5: 0
    
#     y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
#     put_seq_on_board(board, y, x, d_y, d_x, length, "b")
#     print_board(board)
#     analysis(board)
    
#     # Expected output:
#     #        *0|1|2|3|4|5|6|7*
#     #        0 | | | | |w|b| *
#     #        1 | | | | | | | *
#     #        2 | | | | | | | *
#     #        3 | | | | |b| | *
#     #        4 | | | |b| | | *
#     #        5 | |w| | | | | *
#     #        6 | |w| | | | | *
#     #        7 | |w| | | | | *
#     #        *****************
#     #
#     #         Black stones:
#     #         Open rows of length 2: 1
#     #         Semi-open rows of length 2: 0
#     #         Open rows of length 3: 0
#     #         Semi-open rows of length 3: 0
#     #         Open rows of length 4: 0
#     #         Semi-open rows of length 4: 0
#     #         Open rows of length 5: 0
#     #         Semi-open rows of length 5: 0
#     #         White stones:
#     #         Open rows of length 2: 0
#     #         Semi-open rows of length 2: 0
#     #         Open rows of length 3: 0
#     #         Semi-open rows of length 3: 1
#     #         Open rows of length 4: 0
#     #         Semi-open rows of length 4: 0
#     #         Open rows of length 5: 0
#     #         Semi-open rows of length 5: 0
#     #     
    
#     y = 5; x = 3; d_x = -1; d_y = 1; length = 1
#     put_seq_on_board(board, y, x, d_y, d_x, length, "b");
#     print_board(board);
#     analysis(board);
    
#     #        Expected output:
#     #           *0|1|2|3|4|5|6|7*
#     #           0 | | | | |w|b| *
#     #           1 | | | | | | | *
#     #           2 | | | | | | | *
#     #           3 | | | | |b| | *
#     #           4 | | | |b| | | *
#     #           5 | |w|b| | | | *
#     #           6 | |w| | | | | *
#     #           7 | |w| | | | | *
#     #           *****************
#     #        
#     #        
#     #        Black stones:
#     #        Open rows of length 2: 0
#     #        Semi-open rows of length 2: 0
#     #        Open rows of length 3: 0
#     #        Semi-open rows of length 3: 1
#     #        Open rows of length 4: 0
#     #        Semi-open rows of length 4: 0
#     #        Open rows of length 5: 0
#     #        Semi-open rows of length 5: 0
#     #        White stones:
#     #        Open rows of length 2: 0
#     #        Semi-open rows of length 2: 0
#     #        Open rows of length 3: 0
#     #        Semi-open rows of length 3: 1
#     #        Open rows of length 4: 0
#     #        Semi-open rows of length 4: 0
#     #        Open rows of length 5: 0
#     #        Semi-open rows of length 5: 0


  
            
# if __name__ == '__main__':
#    # play_gomoku(8)
#     easy_testset_for_main_functions()
#     #some_tests()
#     # board= make_empty_board(8)
#     # put_seq_on_board(board, 1, 5, 1,0, 3, "w")
#     # print_board(board)
#     # print(detect_row(board, "w", 0, 5, 3, 1, 0))
# # def test_detect_row():
# #     board = make_empty_board(8)
# #     x = 5; y = 1; d_x = 0; d_y = 1; length = 3
# #     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
# #     print_board(board)
# #     if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print(detect_row(board, "w", 0,x,length,d_y,d_x))

test_detect_row()
    
