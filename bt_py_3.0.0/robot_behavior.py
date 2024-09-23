#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt as bt
import bt_library as btl

# Instantiate the tree according to the assignment. The following are just examples.

# Example 1:
# tree_root = bt.Timer(5, bt.FindHome())

# Example 2:
# tree_root = bt.Selection(
#     [
#         BatteryLessThan30(),
#         FindHome()
#     ]
# )

# Example 3:
# tree_root = bt.Selection(
#     [
#         bt.BatteryLessThan30(),
#         bt.Timer(10, bt.FindHome())
#         # GO HOME
#         # CHARGE
#     ]
# )


# subtree 1 implementation
subtree1 = bt.Sequence(
    [
        bt.BatteryLessThan30(),
        bt.Timer(10, bt.FindHome()),
        bt.GoHome(),
        bt.Charge()
    ]
)

# subtree 2 implementation

# subtree 2 level 5
subtree2_2_1_1_1 = bt.Sequence(
    [
        bt.DustySpot(),
        bt.Timer(35, bt.CleanSpot()),
        bt.AlwaysFail()
    ]
)

# subtree 2 level 4
subtree2_2_1_1 = bt.Priority(
    [
        subtree2_2_1_1_1,
        bt.UntilSucceeds(bt.CleanFloor())
    ]
)

# subtree 2 level 3
subtree2_2_1 = bt.Sequence(
    [
        subtree2_2_1_1,
        bt.DoneGeneral()
    ]
)

# subtree 2 level 2
subtree2_1 = bt.Sequence(
    [
        bt.SpotCleaning(),
        bt.Timer(20, bt.CleanSpot()),
        bt.DoneSpot()
    ]
)

subtree2_2 = bt.Sequence(
    [
        bt.GeneralCleaning(),
        subtree2_2_1
    ]
)

# subtree 2 level 1
subtree2 = bt.Selection(
    [subtree2_1,
     subtree2_2]
)


# tree root
tree_root = bt.Priority(
    [
        subtree1,
        subtree2,
        bt.DoNothing()
    ]
)
'''QUESTION'''
# 1. how to implement the priority queue - you implement it yourself
# 2. are we supposed to implement the Go HOME and ChARGE classes ourselves? Yes. Can just be a print statement
# 3. how does the battery level change every second? you define it
# 4. if priority subtree1 is the tree root, then is subtree2 the child of subtree1 and subtree3 that of subtree2
# 5. why are we using the selection composite in line 25? - This is just an example

# Store the root node in a behavior tree instance
robot_behavior = btl.BehaviorTree(tree_root)
