#!/bin/python3
def findDirtyCellPosition(r,c,board):
### Finds the index positions of the dirty cells
    position = []
    row_index = 0
    for row in board:
        if 'd' in row:
            for i in range(len(row)):
                if row[i] == 'd':
                    position.append(row_index)
                    position.append(i)
                    break
            break
        row_index += 1
    return position

def nextMove(posr, posc, board):
    dirty_cell_position = findDirtyCellPosition(posr, posc, board)
    # print(dirty_cell_position)
    row_movement = posr - dirty_cell_position[0]
    # print(row_movement)
    col_movement = posc - dirty_cell_position[1]
    # print(col_movement)
    
    # If dirtyi cell in same row
    if row_movement == 0:
        if col_movement == 0:
            print("CLEAN")
        elif col_movement < 0:
            print("RIGHT")
        elif  col_movement > 0:
            print("LEFT")
    
    # If dirty cell in same column
    elif col_movement == 0:
        if row_movement < 0:
            print("DOWN")
        elif row_movement > 0:
            print("UP")
    
    # If dirty cell not in same row or column
    else:
        if row_movement > 0:
            print("UP")
        elif row_movement < 0:
            print("DOWN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)