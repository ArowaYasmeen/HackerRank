#!/usr/bin/python

def findDirtyCellPositions(r,c,board):
### Finds the index positions of the dirty cells
    positions = []
    row_index = 0
    for row in board:
        if 'd' in row:
            for i in range(len(row)):
                if row[i] == 'd':
                    positions.append([row_index,i])
        row_index += 1
    return positions

def findClosestDirtyCell(r,c,positions):
### Finds the closest dirty cell and removes it from list of dirty cell positions
    min_manhattan_distance = 8
    index = 0
    for i, position in enumerate(positions):
        row_distance = abs(position[0] - r)
        col_distance = abs(position[1] - c)
        manhattan_distance = row_distance + col_distance
        if manhattan_distance < min_manhattan_distance:
            min_manhattan_distance = manhattan_distance
            index = i
    coordinates = positions[index]
    return coordinates

def movesToNearestDirtyCell(r,c,coordinates):
### Moves the bot to the nearest dirty cell
    moves = []
    target_x = coordinates[0]
    target_y = coordinates[1]
    # If same position
    if target_x == r and target_y == c:
        moves.append("CLEAN")
    
    # If dirty cell is down
    elif target_x > r:
        # Down
        for i in range(target_x - r):
            moves.append("DOWN")
    
    # If dirty cell is up
    elif target_x < r:
        # UP
        for i in range(r - target_x):
            moves.append("UP")
    
    # If dirty cell is right
    if target_y > c:
        # RIGHT
        for i in range(target_y - c):
            moves.append("RIGHT")
    
    # If dirty cell is left
    elif target_y < c:
        # LEFT
        for i in range(c - target_y):
            moves.append("LEFT")
    return moves

# # Head ends here



def next_move(posr, posc, board):
    all_dirty_cell_positions = findDirtyCellPositions(posr, posc, board)
    print("Dirty Cell Positions")
    print(all_dirty_cell_positions)
    closest_dirty_cell = findClosestDirtyCell(posr, posc, all_dirty_cell_positions)
    print("CLosest Dirty Cell")
    print(closest_dirty_cell)
    moves = movesToNearestDirtyCell(posr, posc, closest_dirty_cell)
    print(moves[0])

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)