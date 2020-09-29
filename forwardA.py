

class State:

    def __init__(self,no_rows, no_columns,target):
        self.prev = None
        self.current = None
        self.position = []
        # heuristics calculation
        self.dist_f = 0
        self.dist_g = 0
        self.state_val = 1
        self.dist_h = abs(no_rows - target[0]) + abs(no_columns - target[1])


    def update_f(self):
        self.dist_f = self.dist_g + self.dist_h

    def update_g(self, newNode_g):
        self.dist_g = newNode_g

class forwardAStar():

    def __init__(self,no_rows, no_columns):
        self.rows = no_rows
        self.cols = no_columns

    def computePath(self):
        path_cost = 0



    def runForwAStar(self,maze,target):
        cost = 0
        path_found= False

        states_grid = ([[State(row,col, target) for row in range(self.rows)] for col in range(self.cols)])
        # print(states_grid)

        state_current = states_grid[maze.source[0]][maze.source[1]]
        state_target = states_grid[maze.target[0]][maze.target[1]]
        # initialsing since the position is at source
        state_current.state_val = 5
        state_target.state_val = 7

        visited_states=[]
        # set the initial position as it is already visited
        visited_states.append(state_current.position)
        while states_grid.position != state_target.position:

            cost +=1
            visited_states.append(state_current.position)
            state_current.update_g()
            state_current.upadte_f()





