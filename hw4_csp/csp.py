

# backtracking by backjumping - keeping track of the most recent conflict set


class sudoku_solver():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.unassigned = {} # a dictionary of variables with value zero that needs to be assigned a value. The variables are keys and their domains are values.
        self.assigned = [] # a list of variables already assigned. Used like a stack. 

    # visualize the current sudoku board
    def print_matrix(self):
        print(self.matrix)

    # adding constraints to other variables when a variable is assigned - change the domains of unassigned variables in self.unassigned
    def add_constraints(self, var):
        new_constraint = self.matrix[var[0]][var[1]]
        ################## TODO
        # add horizontal contraints

        # add vertical constraints

        # add grid constraints
        pass


    def backtracking(self):
        ################## TODO
        pass

    # pick a variable from self.unassigned to assign a value to and add it to self.assigned
    def pick_var(self):
        # choose a variable from unassigned with smallest domain
        ################## TODO
        picked = (0,0) 
        try:
            # choose a value for the variable
            val = self.pick_val(picked)
            # update the matrix
            self.matrix[picked[0]][picked[1]] = val
            self.assigned.append(picked)
            self.add_constraints(picked)
        except:
            pass

    # pick a value for a given variable that affects the least number of unassigned variable's domains. If unable to pick a value, backtracking will be triggered.
    def pick_val(self, var):
        min_harm = float('inf')
        candidate = 0
        possible_solution = False
        for option in self.unassigned[var]:
            # checks if assigned variable with value 'option' invalidates other domains
            harm = self.arc_consistent(var, option)
            if harm:
                possible_solution = True
                if harm < min_harm:
                    min_harm = harm
                    candidate = option

        # if there is no possible assignment, trigger backtracking
        if not possible_solution:
            self.backtracking()
            return False
        return candidate
    
    # returns the number of variables affected if the variable of location loc can be assigned value val and false otherwise.
    def arc_consistent(loc, val):
        ################## TODO
        affected = 0
        # If an affected variable will have an empty domain, return False
        # check # varialbes with affected domains in each row, add it to affected. 

        # check # varialbes with affected domains in each col, add it to affected

        # check # varialbes with affected domains in each grid, add it to affected
        return False
    
    # checks if the sudoku is done
    def check_goal(self):
        for row in self.matrix:
            if 0 in row:
                return False  
        return True

    # executes the algorithm
    def execution(self):
        while not self.check_goal():
            self.pick_var()
        return self.matrix




