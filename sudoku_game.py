def create_board():
    board = []
    row = []
    count = 0
    while True:
        num = int(input('number -'))
        row.append(num)
        count += 1
        if count % 9 == 0:
            board.append(row)
            row = []
        if count > 81:
            break
    return board


board = create_board()


def print_board(list):
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print('_______________________')
            print()
        for y in range(9):
            if y % 3 ==0 and y != 0 and y != 9:
                print(' | ', end="")
            print(list[x][y], end=" ")

        print()


print_board(board)
print()
print('_____________________________________')
print()


def valid(list, num, pos):
    #checking in row
    for col in range(len(list[0])):
        if num == list[pos[0]][col] and col != pos[1]:

            return False

    #checking in col
    for row in range(len(list[0])):
        if num == list[row][pos[1]] and row != pos[0]:
            return False

    #checking in box
    x = (pos[0]//3)*3
    y = (pos[1]//3)*3
    for row in range(x, x+3):
        for col in range(y, y+3):
            if num == list[row][col] and row != pos[0] and col != pos[1]:
                return False
    return True


def find_empty(lst):
    pos1 = []
    for row in range(9):
        for col in range(9):
            if lst[row][col] == 0:
                pos = (row, col)
                pos1.append(pos)
    return pos1


def fill_empty(ls):
    pos1 = find_empty(ls)
    row = 0
    col = 0
    while True:
        if col > (len(ls[0])- 1):
            row += 1
            col = 0
        if row == len(ls):
            break
        element = ls[row][col]

        if element == 0:
            count = pos1.index((row, col))
            for num in range(1,10):
                ls[row][col] = num
                pos = (row, col)
                bol = valid(ls, num, pos)
                if bol :
                    break
                elif not bol and num == 9:
                    ls[row][col] = 0
                    slicer = count
                    runner = True
                    while runner:
                        pos = pos1[slicer - 1]
                        slicer -= 1
                        row = pos[0]
                        col = pos[1]
                        num = ls[pos[0]][pos[1]]
                        if num != 9:
                            for num in range(num + 1, 10):
                                bol = valid(ls, num, pos)
                                if bol :
                                    ls[pos[0]][pos[1]] = num
                                    runner = False
                                    break
                                elif not bol and num == 9:
                                    ls[pos[0]][pos[1]] = 0
                        elif num == 9:
                            ls[pos[0]][pos[1]] = 0

        col += 1
    return ls


print_board(fill_empty(board))