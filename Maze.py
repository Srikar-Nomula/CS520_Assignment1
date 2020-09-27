import numpy as np
# Generating linked list
import matplotlib.pyplot as plot
class linkedList:

    #initialising the default functions
    def __init__(self):
            self.head = None

class Node:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

# generating maze environments of size 101 x 101
class maze:

    def __init__(self, no_rows,no_columns):
        self.no_rows = no_rows
        self.no_columns= no_columns
        self.maze = self.generate_maze()

    def generate_maze(self):
        # maze = np.ones((101,101))
        maze = np.random.uniform(size=(self.no_rows, self.no_columns))
        # print(maze)
        # maze = [[1 for j in range(self.no_columns)] for i in range(self.no_rows) if np.random.random([101] > 0.3 )]
        for row in range(self.no_rows):
            for col in range(self.no_columns):
                if maze[row][col] < 0.3:
                    maze[row][col] = 0
                else:
                    maze[row][col] = 1

        # Generating source and target
        source = np.random.randint(0,self.no_rows), np.random.randint(0,self.no_columns)
        print(source)

        target = np.random.randint(0, self.no_rows), np.random.randint(0, self.no_columns)
        while ( source == target ):
            target = np.random.randint(0, self.no_rows), np.random.randint(0, self.no_columns)
        print(target)

        # Marking source and target in the grid
        maze[source[0],source[1]] = 5
        maze[target[0], target[1]] = 7
        print(maze)
    def printMaze(maze):
        plot.imshow(maze)







