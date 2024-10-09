Author: Nanxi Liu

1. To run the robot, run main.py. User request for general cleaning and spot cleaning can be made before the while loop in main.py by setting
the variable GENERAL_CLEANING and SPOT_CLEANING to True in line 18 and 19.
2. the priority composite is implemented such that the argument (list of nodes) it takes in is already in
order of descending priority, with the most prioritized node at the beginning.
3. the clean floor task fails with a probability of 0.15.
4. the battery charges faster than it depletes. Its charging speed is 10%/iteration and depleting speed is 1%/iteration.
5. the robot stops running after it's completed all the tasks. Users can also choose to just let the robot charge and not do any tasks.