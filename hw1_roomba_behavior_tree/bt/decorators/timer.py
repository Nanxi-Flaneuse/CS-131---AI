#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode


class Timer(Decorator):
    """
    Specific implementation of the timer decorator.
    """
    TIMER_NOT_IN_USE = -1

    __time: int

    def __init__(self, time: int, child: TreeNode):
        """
        Default constructor.

        :param time: Duration of the timer [counts]
        :param child: Child associated to the decorator
        """
        super().__init__(child)

        self.__time = time

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        # If there is no state for the timer or the timer is not in use,
        # the current time is what the timer decorator was defined with
        timer_period = self.additional_information(blackboard, Timer.TIMER_NOT_IN_USE)
        time_to_expiration = timer_period if timer_period > Timer.TIMER_NOT_IN_USE else self.__time

        # Advance the time
        time_to_expiration = time_to_expiration - 1

        # If the timer expired, do not evaluate the child.
        # Just return immediately with a successful result
        if time_to_expiration < 0:
            return self.report_succeeded(blackboard, Timer.TIMER_NOT_IN_USE)

        # Evaluate the child
        self.print_message(f"time-to-expiration = {time_to_expiration}")
        result_child = self.child.run(blackboard)

        # If the child failed, terminate immediately the timer
        return self.report_failed(blackboard, Timer.TIMER_NOT_IN_USE) \
            if result_child == ResultEnum.FAILED \
            else self.report_running(blackboard, time_to_expiration)
