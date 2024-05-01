import heapq

class Node:
    def __init__(self, m, x, y, newX, newY, level, parent):
        self.parent = parent
        self.m = [row[:] for row in m]
        self.m[x][y], self.m[newX][newY] = self.m[newX][newY], self.m[x][y]
        self.x = newX
        self.y = newY
        self.level = level
        self.cost = float('inf')

def printMatrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def calculateCost(initialM, finalM):
    count = 0
    for i in range(len(initialM)):
        for j in range(len(initialM[0])):
            if initialM[i][j] != 0 and initialM[i][j] != finalM[i][j]:
                count += 1
    return count

def isSafe(x, y):
    return 1 if 0 <= x < N and 0 <= y < N else 0

def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.m)
    print()

def solve(initialM, x, y, finalM):
    pq = []
    heapq.heapify(pq)

    root = Node(initialM, x, y, x, y, 0, None)
    root.cost = calculateCost(initialM, finalM)

    heapq.heappush(pq, (root.cost + root.level, id(root), root))

    while pq:
        min_cost, _, min_node = heapq.heappop(pq)
        
        if min_node.cost == 0:
            printPath(min_node)
            return

        for i in range(4):
            newX, newY = min_node.x + row[i], min_node.y + col[i]
            if isSafe(newX, newY):
                child = Node(min_node.m, min_node.x, min_node.y, newX, newY, min_node.level + 1, min_node)
                child.cost = calculateCost(child.m, finalM)
                heapq.heappush(pq, (child.cost + child.level, id(child), child))

N = 3
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

initialM = [
    [0, 1, 2],
    [4, 5, 8],
    [6, 7, 3]
]

finalM = [
    [0, 3, 7],
    [4, 2, 5],
    [6, 8, 1]
]

x, y = 1, 2

solve(initialM, x, y, finalM)


# Output :
# 0 1 2
# 4 5 8
# 6 7 3

# 0 1 2
# 4 5 3
# 6 7 8

# 0 1 2
# 4 5 3
# 6 8 7

# 0 1 2
# 4 8 3
# 6 5 7

# 0 8 2
# 4 1 3
# 6 5 7

# 0 2 8
# 4 1 3
# 6 5 7

# 0 2 3
# 4 1 8
# 6 5 7

# 0 2 3
# 4 1 7
# 6 5 8

# 0 2 3
# 4 1 7
# 6 8 5

# 0 2 3
# 4 8 7
# 6 1 5

# 0 8 3
# 4 2 7
# 6 1 5

# 0 3 8
# 4 2 7
# 6 1 5

# 0 3 7
# 4 2 8
# 6 1 5

# 0 3 7
# 4 2 5
# 6 1 8

# 0 3 7
# 4 2 5
# 6 8 1
