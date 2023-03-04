#!/usr/bin/python
import math 
def displayPathtoPrincess(n,grid):
#print all the moves here

    actions = []
    i = math.floor(n/2)
    j = math.floor(n/2)
    
    # Princess in top left
    if grid[0][0] == 'p':
        while i >= 0:
            if i == 0:
                while j > 0:
                    actions.append("LEFT")
                    j -= 1
            else:
                actions.append("UP")
            i -= 1

    # Princess in top right
    elif grid[0][n - 1] == 'p':
        while i >= 0:
            if i == 0:
                while j < n - 1:                
                    actions.append("RIGHT")
                    j += 1
            else:
                actions.append("UP")
            i -= 1
    
    # Princess in bottom left
    elif grid[n - 1][0] == 'p':
        while i <= n - 1:
            if i == n - 1:
                while j > 0:
                    actions.append("LEFT")
                    j -= 1
            else:
                actions.append("DOWN")
            i += 1    

    # Princess in bottom right
    elif grid[n - 1][n - 1] == 'p':
        while i <= n - 1:
            if i == n - 1:
                while j < n - 1:
                    actions.append("RIGHT")
                    j += 1
            else:
                actions.append("DOWN")
            i += 1  

    for action in actions:
        print(action)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)