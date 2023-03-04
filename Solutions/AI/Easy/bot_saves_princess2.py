#

def nextMove(n,r,c,grid):
    princess_row = 0
    for row in grid:
        if 'p' in row:
            princess_col = row.index('p')
            break
        else:
            princess_row += 1
    # print("Location of princess is " + str(princess_row) + ' ' + str(princess_col))

    if princess_row == r:
        if princess_col < c:
            print("LEFT")
        elif princess_col > c:
            print("RIGHT")
        elif princess_col == c:
            pass
    elif princess_row > r:
        print("DOWN")
    elif princess_row < r:
        print("UP")
    

    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))