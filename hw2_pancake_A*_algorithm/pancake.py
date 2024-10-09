'''10/9/2024 Nanxi Liu'''


# Implementation of Priority Queue using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

	# for inserting an element in the queue
    def insert(self, data): self.queue.append(data)

    # pops the element with smallest cost (highest priority) from the queue and returns it.
    def delete(self):
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i].get_cost() < self.queue[min_val].get_cost():
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print('error encountered')
            exit()

    # search through the queue to see if a modified pancake list with higher cost already exists
    def search_replace(self, stack):
        for ind in range(len(self.queue)):
             if self.queue[ind].get_curr() == stack.get_curr() and self.queue[ind].get_cost() > stack.get_cost():
                  self.queue[ind] = stack
                  break
    
    # checks if an item has the same child as one of the items in the queue
    def check(self,pc):
        for node in self.queue:
            if node.get_curr() == pc.get_curr():
                return True
        return False
    
    # returns the queue in a readable format
    def get_queue(self):
        return [x.get_pancake() for x in self.queue]

# a class to keep track of visited nodes   
class Visited():
    def __init__(self) -> None:
        self.vis = []

    # append an item to visited
    def append(self, pc):
        self.vis.append(pc)
    
    # checks if a given node has been visited
    def check(self,pc):
        for node in self.vis:
            if node.get_prev() == pc.get_prev() and node.get_action() == pc.get_action():
                return True
        return False
    
# class for pancake objects
class Pancake():

    # the constructor takes in 4 arguments 
    # @parent - the parent node of the current node, which is also a pancake object 
    # @ind - an index where the flip action will take place, 
    # @prev - the current state of the pancake number arrangements
    # @algo - the algorithm that will determine the cost function - either A star or UCS.
    def __init__(self, parent, ind, prev, algo='a*'):
        self.index = ind
        self.prev = prev
        self.algo = algo
        self.num = len(prev)

        # get the child state of the pancake
        self.curr = self.flip(self.index)

        # get the cost for performing the action
        self.cost = self.total_cost()
        self.parent = parent
        

    def get_pancake(self):
        return (self.index,self.prev)
    def get_cost(self):
        return self.cost
    def get_action(self):
        return self.index
    def get_curr(self):
        return self.curr
    def get_prev(self):
        return self.prev
    def get_num(self):
        return self.num
    def get_parent(self):
        return self.parent

    # cost function depending on the kind of algorithm. UCS always has a backward cost of 1 for taking any action and A star 0. 
    def total_cost(self):
        if self.algo == 'ucs':
            return 1
        else:
            return self.get_heur()
    
    # gap heuristics function
    def get_heur(self):
        gap = 0
        for i in range(1,len(self.curr)):
            if abs(self.curr[i] - self.curr[i-1]) > 1:
                gap += 1
        if self.curr[0] != 10:
            gap += 1
        return gap

    # function that performs the flip action. 
    def flip(self,i):
        flipped = list(reversed(self.prev[i:]))
        return self.prev[0:i] + flipped


# helper function: updates the frontier with children of the current node
def update_frontier(frontier,stack, visited_nodes, type):
    for i in range(stack.get_num()-1):
        new_state = Pancake(stack, i, stack.get_curr(), type)
        # if child is not in frontier or visited
        if not visited_nodes.check(new_state) and not frontier.check(new_state):
            frontier.insert(new_state)
        # else if child is in frontier with higher cost
        else:
            frontier.search_replace(new_state)

    return frontier

# helper function that traces back all the parents of a node and return a list of the path
def get_solution(node):
    sol = [node.get_pancake()]
    temp = node.get_parent()
    while temp != None:
        sol.append(temp.get_pancake())
        temp = temp.get_parent()
    return list(reversed(sol))

# search function that performs a search when given a list of numbers in any order from 1 to 10 and the type of algorithm
def search(pancakes, type):
    # checks if the input is valid
    if sorted(pancakes) == [1,2,3,4,5,6,7,8,9,10] and (type in ['a*','ucs']):
    # initialize the frontier with a list of back and forward cost for each node
        frontier = PriorityQueue()
        for i in range(len(pancakes)-1):
            # each priority node contains 4 things: cost of the action, action, resulted state, and previous state
            frontier.insert(Pancake(None,i, pancakes,type))
        print('frontier initialized')
        # solution = Solution()
        visited = Visited()
        choice = Pancake(None, 9, pancakes,type)
        print('searching begins')
        while choice.get_heur() != 0:
            if len(frontier.queue) == 0:
                return None
            else:
                # pops an element off the priority queue. append it to visited
                choice = frontier.delete()
                visited.append(choice)

                # checks if choice is the goal state
                if choice.get_heur() == 0:
                    # get path
                    solution = get_solution(choice)
                    print('number of steps:',str(len(solution)))
                    return solution
                else:
                    frontier = update_frontier(frontier, choice, visited, type)
    else:
        print('Invalid input. The pancake stack should be a list of numbers from 1 to 10 in any order. The algorithm type input should only be a* or ucs')
        return None
        

if __name__ == '__main__':
    print(search([10,9,8,6,2,3,1],'a*'))
    print(search([10,9,8,6,7,5,4,2,3,1],'a star'))
    print(search([10,9,8,6,7,5,4,2,3,1],'a*'))
    print(search([10,9,8,7,6,5,4,2,3,1],'ucs'))
    print(search([7,3,5,8,2,9,1,4,6,10],'a*'))





'''References
[1] https://www.geeksforgeeks.org/priority-queue-in-python/
[2] https://www.geeksforgeeks.org/python-find-the-tuples-containing-the-given-element-from-a-list-of-tuples/
[3] backward function and solution tree reference: https://github.com/Frama-99/Pancake-Problem---A-Star/blob/master/pancake.py
 '''
