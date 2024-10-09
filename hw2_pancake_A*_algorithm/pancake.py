# how do we define an optimal solution? ie. least number of flips?
# does flip mean reversing the entire order of the pancakes above the spatula?


# 5
# 3
# 8
# 6
# 7
# 9
# 1
# 2
# 4
# 10

# the cost of performing a flip action at any given position - based on the index of the position
def get_back_cost(ind, pancakes):
    # return 1
    return len(pancakes) - ind

# heuristic function. checked
def get_heur(pancakes):
    gap = 0
    # value 11 is the bottom plate
    # temp = pancakes
    # temp.insert(0,11)
    for i in range(1,len(pancakes)):
        if abs(pancakes[i] - pancakes[i-1]) > 1:
            gap += 1
    if pancakes[0] != 10:
        gap += 1
    return gap

# get a sum of the backward and forward cost. checked
def total_cost(ind, pancakes):
    return get_back_cost(ind, pancakes) + get_heur(pancakes)

# function that performs the flip action. checked
def flip(ind, pancakes):
    flipped = list(reversed(pancakes[ind:]))
    return pancakes[0:ind] + flipped

# updates the frontier with children of the current node
def update_frontier(frontier,stack, visited):
    for i in range(stack.get_num()):
        # each priority node contains 4 things: cost of the action, action, resulted state, and previous state
        flipped = stack.flip(0)
        cost = stack.total_cost(i) + stack.get_cost()
        # if child is not in the frontier or visited then
        new_state = Pancake(cost,i, flipped, stack.get_curr())
        if flipped != stack.get_prev() and new_state not in visited:
            frontier.insert(new_state)
        # else if child is in frontier with higher cost
        else:
            ind = frontier.search(new_state)
            if ind:
                frontier.replace(ind, new_state)
    return frontier

# A simple implementation of Priority Queue using Queue. All methods tested and works.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    

	# for inserting an element in the queue
    def insert(self, data): self.queue.append(data)
          
	# for popping an element based on Priority
    # def delete(self):
    #     try:
    #         min_val = 0
    #         for i in range(len(self.queue)):
    #             if self.queue[i] < self.queue[min_val]:
    #                 min_val = i
    #         item = self.queue[min_val]
    #         del self.queue[min_val]
    #         return item
    #     except IndexError:
    #         print('error encountered')
    #         exit()

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

    # replace an element in the queue with another element
    def replace(self,ind,element):
        self.queue[ind] = element

    # search through the queue to see if a modified pancake list with higher cost already exists
    def search(self, stack):
        for ind in range(len(self.queue)):
             if self.queue[ind].get_curr() == stack.get_curr() and self.queue[ind].get_cost() > stack.get_cost():
                  return ind
        return False

# a class for the search solution
class Solution():
    def __init__(self):
        self.sol = []

    # checks if an existing node with 
    def add(self, stack):

        # find first node in sol that has its prev pancake as your prev pancake and delete it
        for i in range(len(self.sol)):
            if self.sol[i].get_prev() == stack.get_prev():
                del self.sol[i:]
                break
        # append yours to the list
        self.sol.append(stack)

    def get_sol(self):
        return [x.get_pancake() for x in self.sol]

    # def delete(self, flipped, cost):
    #     for i in range(len(self.sol)):
    #         if self.sol[i][0] > cost and self.sol[i][2] == flipped:
    #             del self.sol[i:]
    #             break
    

class Pancake():
    def __init__(self, cost, ind, curr, prev):
        self.state = (cost, ind, curr, prev)
        self.cost = cost
        self.index = ind
        self.curr = curr
        self.prev = prev
        self.num = len(curr)

    def get_pancake(self):
        return self.state
    def get_cost(self):
        return self.state[0]
    def get_action(self):
        return self.state[1]
    def get_curr(self):
        return self.state[2]
    def get_prev(self):
        return self.state[3]
    def get_num(self):
        return self.num
    
        # the cost of performing a flip action at any given position - based on the index of the position
    def get_back_cost(self, i):
        # return 1
        return self.num - i

    # heuristic function. checked
    def get_heur(self):
        gap = 0
        # value 11 is the bottom plate
        # temp = pancakes
        # temp.insert(0,11)
        for i in range(1,len(self.curr)):
            if abs(self.curr[i] - self.curr[i-1]) > 1:
                gap += 1
        if self.curr[0] != 10:
            gap += 1
        return gap

    # get a sum of the backward and forward cost. checked
    def total_cost(self, i):
        return self.get_back_cost(i) + self.get_heur()

    # function that performs the flip action. checked
    def flip(self,i):
        flipped = list(reversed(self.curr[i:]))
        return self.curr[0:i] + flipped




def a_star(pancakes):
    # initialize the frontier with a list of back and forward cost for each node
    frontier = PriorityQueue()
    for i in range(len(pancakes)):
          # each priority node contains 4 things: cost of the action, action, resulted state, and previous state
          frontier.insert(Pancake(total_cost(i, pancakes),i, flip(i, pancakes), pancakes))#(total_cost(i, pancakes),i, flip(i, pancakes), pancakes))
    # found_solution = False
    print('frontier initialized')
    solution = Solution()
    visited = []
    choice = Pancake(0,9,pancakes, pancakes)#pancakes
    print('searching begins')
    while choice.get_heur() != 0:
        print(frontier.queue)
        if len(frontier.queue) == 0:
            return None
        else:
            # pop an element off the priority queue. append it to solution
            choice = frontier.delete()
            # print(choice)
            visited.append(choice)
            solution.add(choice)
            # updated pancakes
            # pancakes_curr = choice.get_curr()
            # pancakes_prev = choice.get_prev()
            # cost = choice.get_cost()
            # check if flipped pancakes statsfies goal state
            if choice.get_heur() == 0:
                return solution.get_sol()
            else:
                frontier = update_frontier(frontier, choice, visited)
              



def ucs():
    pass


if __name__ == '__main__':
    # testing get_heur
    # print(get_heur([9,10,8,7,6,4,5,3,2,1]))
    # testing flip
    # print(flip(2,[1,3,2,4,5,7,6,8,9,10]))
    # testing queue
    # myQueue = PriorityQueue()
    # c1 = Pancake(12,1,[1,3,2,4,5,7,6,8,9,10],[1,3,2,4,5,7,6,8,9,10])
    # c2 = Pancake(15,1,[1,3,2,5,4,7,6,8,9,10],[1,3,2,4,5,7,6,8,9,10])
    # myQueue.insert(c1)
    # myQueue.insert(c2)
    # myQueue.insert((12,1,[1,3,2,4,5,7,6,8,9,10],[1,3,2,4,5,7,6,8,9,10]))
    # myQueue.insert((1,1,[0,3,2,4,5,7,6,8,9,10],[1,3,2,4,5,7,6,8,9,10]))
    # myQueue.insert((15,1,[1,3,2,5,4,7,6,8,9,10],[1,3,2,4,5,7,6,8,9,10]))
    # print(myQueue.queue)
    # print('------------------------------------------------')
    # print(update_frontier(myQueue, [0,3,2,4,5,7,6,10,9,8], [0,3,2,4,5,7,6,8,9,10], [],100))
    
    # print(myQueue.queue)
    # print(myQueue.search([1,3,2,5,4,7,6,8,9,10],10))
    # print(myQueue.queue)
    # myQueue.replace(1,(2,1,[1,3,2,4,5,7,6,8,9,10],[1,3,2,4,5,7,6,8,9,10]))
    # print(myQueue.queue)
    # print(myQueue.delete().get_pancake())
    print(a_star([10,9,8,7,6,5,4,2,1,3]))




'''References
[1] https://www.geeksforgeeks.org/priority-queue-in-python/
[2] https://www.geeksforgeeks.org/python-find-the-tuples-containing-the-given-element-from-a-list-of-tuples/
 '''
