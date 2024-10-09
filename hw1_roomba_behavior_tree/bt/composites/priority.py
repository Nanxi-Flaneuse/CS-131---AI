#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl


class Priority(btl.Composite):
    """
    Specific implementation of the priority composite.
    """

    def __init__(self, children: btl.NodeListType):
        """
        Default constructor.

        :param children: List of children for this node. Children are listed in sequence of priority. With the highest priority child being the first and the rest follows by level of their priority
        :param priority_list: a list consisting of priorities corresponding to each child. Priority starts
        from 1 and increases by 1, with 1 being the highest priority and 
        """
        super().__init__(children)
        # self.priority = {}
        # for ind in range(children):
        #     priority[]

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        for child_position in range(len(self.children)):
            child = self.children[child_position]

            result_child = child.run(blackboard)
            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

        return self.report_failed(blackboard, 0)