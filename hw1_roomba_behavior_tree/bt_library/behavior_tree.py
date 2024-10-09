#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - Copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#
from typing import Optional

from .blackboard import Blackboard
from .common import ResultEnum
from .tree_node import TreeNode


class BehaviorTree:
    """
    The base behavior tree class.
    """
    __root: Optional[TreeNode]  # Behavior tree root

    def __init__(self, root: Optional[TreeNode]):
        """
        Default constructor.

        :param root: Root node of the behavior tree.
        """
        self.__root = root

    @property
    def root(self) -> Optional[TreeNode]:
        """
        :return: Return the behavior tree root node
        """
        return self.__root

    def evaluate(self, blackboard: Blackboard) -> ResultEnum:
        """
        Evaluate the whole behavior tree.

        :param blackboard: Blackboard with the current state to query
        :return: The result of the evaluation
        """
        return self.__root.run(blackboard) if self.__root else ResultEnum.FAILED
