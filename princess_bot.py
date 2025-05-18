def displayPathtoPrincess(n,grid):
    pos_p = []
    pos_m = []
    row = {
        0 : "UP",
        n-1 : "DOWN"
    }
    col = {
        0 : "LEFT",
        n-1 : "RIGHT"
    }
    for i in (0,n-1):
        for j in (0,n-1):
            if (grid[i][j] == "p"):
                pos_p = [i,j]
                direction = [row[i], col[j]]
                break
        else:
            continue
        break
            
    middle=int(n/2)
    for i in (middle, middle+1):
        for j in (middle, middle+1):
            if (grid[i][j] == "m"):
                pos_m = [i,j]
                break
        else:
            continue
        break
    for i in range (2):
        for j in range(abs(pos_m[i] - pos_p[i])):
            print(direction[i])

m = int(input())
grid = ['----p', '-----', '--m--', '-----', '-----'] 
#for i in range(0, m): 
#    grid.append(input().strip())
displayPathtoPrincess(m,grid)

