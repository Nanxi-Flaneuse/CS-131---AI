#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from typing import List

from .tree_node import TreeNode

NodeListType = List[TreeNode]  # Type definition for a list of tree nodes


class Composite(TreeNode):
    """
    The generic definition of a composite tree node class.
    """
    __children: NodeListType  # List of children of the composite

    def __init__(self, children: NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__()

        self.__children = children

    @property
    def children(self) -> NodeListType:
        """
        :return: Return the list of children in the composite
        """
        return self.__children
