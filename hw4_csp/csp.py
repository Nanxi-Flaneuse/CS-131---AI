'''Author: Nanxi Liu. Date: Nov/7/2024'''

class sudoku_solver():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.unassigned = self.get_domain() # a dictionary of variables with value zero that needs to be assigned a value. The variables are keys and their domains are values.
        self.assigned_domain = {} # a dictionary of assigned variables with their original domains
        self.assigned_var = [] # a list of variables already assigned. Used like a stack. 
        self.tried = {} # each element has a tried list that contains all the possible values it's tried. tried list starts out with empty lists for all variables. Each time the var is assigned a value, the value is added to tried. Tried is emptied when performing backtracking.
        self.conflicts = {} # a dictionary that keeps track of variable assignments that caused the key variable to loose a value in its domain. Created for the purpose of restoring domains. key: variable, value: a list of variables
        # fill in self.tried and self.conflicts
        try:
            for i in range(9):
                for j in range(9):
                    if self.matrix[i][j] == 0:
                        self.tried[(i,j)] = []
                        self.conflicts[(i,j)] = []
        except:
            pass
            # print('matrix has wrong format')

    # helper function: visualize the current sudoku board
    def print_matrix(self):
        for row in self.matrix:
            print(row)

    # helper function: returns the range of indices of the grid that the coordinate is in. For instance, for coordinate (3,3), the function returns [[3,4,5],[3,4,5]]
    def find_grid(self, coor):
        result = []
        if coor[0] < 3:
            result.append([0,1,2])
        elif coor[0] < 6:
            result.append([3,4,5])
        else:
            result.append([6,7,8])

        if coor[1] < 3:
            result.append([0,1,2])
        elif coor[1] < 6:
            result.append([3,4,5])
        else:
            result.append([6,7,8])
        return result

    # helper function: fill in the initial domain
    def get_domain(self):
        try:
            domain = {}
            for i in range(9):
                for j in range(9):
                    if self.matrix[i][j] == 0:
                        domain[(i,j)] = [1,2,3,4,5,6,7,8,9]
                        # check row
                        for ele in self.matrix[i]:
                            if ele != 0:
                                try:
                                    domain[(i,j)].remove(ele)
                                except:
                                    pass
                        # check col
                        for coor in [(x,j) for x in range(9)]:
                            col_ele = self.matrix[coor[0]][coor[1]]
                            if col_ele != 0:
                                try:
                                    domain[(i,j)].remove(col_ele)
                                except:
                                    pass
                        # check grid
                        grid = self.find_grid((i,j))
                        for r in grid[0]:
                            for c in grid[1]:
                                grid_ele = self.matrix[r][c]
                                if grid_ele != 0:
                                    try:
                                        domain[(i,j)].remove(grid_ele)
                                    except:
                                        pass
            return domain
        except:
            pass
            # print('matrix has wrong format')
                    


    # adding constraints to other variables when a variable is assigned - change the domains of unassigned variables in self.unassigned
    def add_constraints(self, var):
        new_constraint = self.matrix[var[0]][var[1]]
        # in each step, for all variables affected by var's new assignment, add the coordinates of the variables to conflicts[var]
        # add horizontal contraints
        for j in range(0,9):
            try:
                if new_constraint in self.unassigned[(var[0],j)]:
                    self.unassigned[(var[0],j)].remove(new_constraint)
                    self.conflicts[var].append((var[0],j))
            except:
                pass
        # add vertical constraints
        for row_ind in range(0,9):
            try:
                if new_constraint in self.unassigned[(row_ind,var[1])]:
                    self.unassigned[(row_ind,var[1])].remove(new_constraint)
                    self.conflicts[var].append((row_ind,var[1]))
            except:
                pass

        # add grid constraints
        grid = self.find_grid(var)
        for r in grid[0]:
            for c in grid[1]:
                try:
                    if new_constraint in self.unassigned[(r,c)]:
                        self.unassigned[(r,c)].remove(new_constraint)
                        self.conflicts[var].append((r,c))
                except:
                    pass

    # removes constraints added to variables in self.unassigned when the last variable was assigned a value
    def remove_constraints(self, var):
        rem_constraint = self.matrix[var[0]][var[1]]
        # use the conflict dictionary, restore value to affected variable's domains
        for coor in self.conflicts[var]:
            self.unassigned[coor].append(rem_constraint)
        # clear the list for the conflict variable
        self.conflicts[var].clear()

    # backtracking function
    def backtracking(self):
        try:
            # print('backtracking')
            latest_conflict = self.assigned_var.pop()
            # put the variable back to unassigned
            self.unassigned[latest_conflict] = self.assigned_domain.pop(latest_conflict, None)
            # remove constraints from unassigned variables in its row, col, and grid
            self.remove_constraints(latest_conflict)
            # reset this variable's value to 0
            self.matrix[latest_conflict[0]][latest_conflict[1]] = 0
            return True
        except:
            print('Backtack failed. No assigned variables yet')
            return False

    # pick a variable from self.unassigned to assign a value to and add it to self.assigned_domain
    def pick_var(self):
        # choose a variable from unassigned with smallest domain
        picked = (0,0) 
        min_len = min([len(self.unassigned[ele]) for ele in self.unassigned])
        for var in self.unassigned.keys():
            if len(self.unassigned[var]) == min_len:
                picked = var
        # choose a value for the variable
        val = self.pick_val(picked)
        # update the matrix if a value can be assigned to the variable
        if val > 0:
            self.matrix[picked[0]][picked[1]] = val
            self.assigned_var.append(picked)
            # remove newly assigned varialbe from unassigned and move it to assigned
            domain = self.unassigned.pop(picked, None)
            # add full domain to assigned
            self.assigned_domain[picked] = domain
            self.add_constraints(picked)
            # add value to tried
            self.tried[picked].append(val)
            return True
        # if there is no possible assignment, trigger backtracking
        else:
            # set tried options for var to empty list
            self.tried[var].clear()
            self.conflicts[var].clear()
            bc = self.backtracking()
            return bc
        

    # pick a value for a given variable that affects the least number of unassigned variable's domains. If unable to pick a value, backtracking will be triggered.
    def pick_val(self, var):
        min_harm = float('inf')
        candidate = 0
        for option in self.unassigned[var]:
            # checks if option is already tried. If not, continue
            if option not in self.tried[var]:
                # checks if assigned variable with value 'option' invalidates other domains
                harm = self.arc_consistent(var, option)
                # assign candidate to current option that cause least affected domains in other variables
                if harm and harm < min_harm:
                    min_harm = harm
                    candidate = option
        return candidate
    
    # returns the number of variables affected if the variable of location loc can be assigned value val and false otherwise.
    def arc_consistent(self, var, val):
        affected = 1 # affected starts from 1 because the number 0 is natually false
        # If an affected variable will have an empty domain, return False
        # check # varialbes with affected domains in each row, add it to affected.
        for j in range(0,9):
            if j != var[1]:
                try:
                    if val in self.unassigned[(var[0],j)]:
                        if len(self.unassigned[(var[0],j)])  > 1:
                            affected += 1
                            # print('affect found in row')
                        else:
                            # print(var,"'s value",val,"conflicts with",(var[0],j),"'s doman",self.unassigned[(var[0],j)])
                            return False
                except:
                    pass
        # check # varialbes with affected domains in each col, add it to affected
        for row_ind in range(0,9):
            if row_ind != var[0]:
                try:
                    if val in self.unassigned[(row_ind,var[1])]:
                        if len(self.unassigned[(row_ind,var[1])])  > 1:
                            affected += 1
                            # print('affect found in col')
                        else:
                            # print(var,"'s value",val,"conflicts with",(row_ind,var[1]),"'s doman",self.unassigned[(row_ind,var[1])])
                            return False
                except:
                    pass

        # check # varialbes with affected domains in each grid, add it to affected
        grid = self.find_grid(var)
        for r in grid[0]:
            for c in grid[1]:
                if r != var[0] and c != var[1]:
                    try:
                        if val in self.unassigned[(r,c)]:
                            if len(self.unassigned[(r,c)])  > 1:
                                affected += 1
                                # print('affect found in grid')
                            else:
                                # print(var,"'s value",val,"conflicts with",(r,c),"'s doman",self.unassigned[(r,c)])
                                return False
                    except:
                        pass
        return affected
    
    # checks if the sudoku is done
    def check_goal(self):
        for row in self.matrix:
            if 0 in row:
                return False  
        return True

    # executes the algorithm
    def execution(self):
        if len(self.matrix) == 9:
            format = True
            # print('length fits')
            print('initial matrix')
            for line in self.matrix:
                print(line)
                if len(line) != 9: 
                    format = False
                for num in line:
                    if num not in [0,1,2,3,4,5,6,7,8,9]:
                        format = False
            if format:
                print('format fits')
                while not self.check_goal():
                    executable = self.pick_var()
                    if not executable:
                        print('sudoku unsolvable')
                        return False
                print('solution')
                self.print_matrix()
                return self.matrix
            else:
                print('Execution failed: input needs to be a 9 by 9 matrix with each value ranging from 0 to 9')
        else:
            print('Execution failed: input needs to be a 9 by 9 matrix with each value ranging from 0 to 9')


if __name__ == '__main__':
    sudoku = [[6,0,8,7,0,2,1,0,0],[4,0,0,0,1,0,0,0,2],[0,2,5,4,0,0,0,0,0],[7,0,1,0,8,0,4,0,5],[0,8,0,0,0,0,0,7,0],[5,0,9,0,6,0,3,0,1],[0,0,0,0,0,6,7,5,0],[2,0,0,0,9,0,0,0,8],[0,0,6,8,0,5,2,0,3]]
    solver = sudoku_solver(sudoku)
    solver.execution()

    sudoku_1 = [[0,7,0,0,4,2,0,0,0],[0,0,0,0,0,8,6,1,0],[3,9,0,0,0,0,0,0,7],[0,0,0,0,0,4,0,0,9],[0,0,3,0,0,0,7,0,0],[5,0,0,1,0,0,0,0,0],[8,0,0,0,0,0,0,7,6],[0,5,4,8,0,0,0,0,0],[0,0,0,6,1,0,0,5,0]]
    solver_1 = sudoku_solver(sudoku_1)
    solver_1.execution()

    # wrong input testing
    sudoku_2 = [[0,7,4,2,0,0,0],[0,0,0,0,0,8,6,1,0],[3,9,0,0,0,0,0,0,7],[0,0,0,0,0,4,0,0,9],[0,0,3,0,0,0,7,0,0],[5,0,0,1,0,0,0,0,0],[8,0,0,0,0,0,0,7,6],[0,5,4,8,0,0,0,0,0],[0,0,0,6,1,0,0,5,0]]
    solver_2 = sudoku_solver(sudoku_2)
    solver_2.execution()

    # wrong input testing
    sudoku_3 = [[0,110,0,7,4,2,0,0,0],[0,0,0,0,0,8,6,1,0],[3,9,0,0,0,0,0,0,7],[0,0,0,0,0,4,0,0,9],[0,0,3,0,0,0,7,0,0],[5,0,0,1,0,0,0,0,0],[8,0,0,0,0,0,0,7,6],[0,5,4,8,0,0,0,0,0],[0,0,0,6,1,0,0,5,0]]
    solver_3 = sudoku_solver(sudoku_3)
    solver_3.execution()



'''references
1. https://stackoverflow.com/questions/24089924/skip-over-a-value-in-the-range-function-in-python
2. https://www.geeksforgeeks.org/constraint-satisfaction-problems-csp-in-artificial-intelligence/'''

