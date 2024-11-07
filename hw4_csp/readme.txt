To execute the sudoku solver, simply run csp.py. The input matrix to the solver can be changed at the end of the file.
The testing code for the solver contains two test cases with bad inputs. In this situation, the solver will return an error statement
The input to the solver has to be a 9 by 9 matrix with each value ranging from 0 to 9
This algorithm uses backjumping to keep track of the most recent conflicts. 
This algorithm uses least constraining value when choosing a value for a variable.
This algorithm chooses the variable with fewest values in the domains during each execution.
This algorithm uses arc consistency to prune illegal assignments.