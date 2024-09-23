#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from typing import Any, Optional

from .blackboard import Blackboard
from .common import NodeIdType, NODE_RESULT, ADDITIONAL_INFORMATION, ResultEnum

__identification_counter__: int = 0


class TreeNode:
    """
    The base node class.
    """
    __id: NodeIdType  # Identification of the node

    def __init__(self):
        """
        Default constructor.
        """
        global __identification_counter__

        self.__id = __identification_counter__
        __identification_counter__ = __identification_counter__ + 1

    def additional_information(self, blackboard: Blackboard, default_value: Optional[Any]) -> Any:
        """
        Return the custom state associated with the node.

        :param blackboard: Blackboard with the current state of the tree
        :param default_value: Value to return if the node state was not found in the blackboard
        :return: State of this node or None if not found
        """
        result = default_value

        if blackboard.is_in_states(self.__id):
            state = blackboard.get_in_states(self.__id)
            if ADDITIONAL_INFORMATION in state:
                result = blackboard.get_in_states(self.__id)[ADDITIONAL_INFORMATION]

        return result

    @property
    def id(self) -> NodeIdType:
        """
        :return: Return the identification of the node
        """
        return self.__id

    @property
    def name(self) -> str:
        """
        :return: Return the name of the class
        """
        return self.__class__.__name__

    @property
    def pretty_id(self) -> str:
        """
        :return: Return the pretty version of the node class and identification
        """
        return f"{self.name}({self.__id})"

    def print_message(self, message: str):
        """
        Print the specified message with a pretty print.

        :param message: Message to print
        """
        print(f"{self.pretty_id}: {message}")

    def report_failed(self, blackboard: Blackboard, additional_information: Any = None):
        """
        Before returning a failed state, print it in a human-readable way.

        :param blackboard: Blackboard with the current state of the problem
        :param additional_information: Additional information for the node to store in the blackboard
        :return: The specified result
        """
        blackboard.set_in_states(
            self.__id,
            {NODE_RESULT: ResultEnum.FAILED, ADDITIONAL_INFORMATION: additional_information}
        )
        self.print_message("FAILED")

        return ResultEnum.FAILED

    def report_running(self, blackboard: Blackboard, additional_information: Any = None):
        """
        Before returning a running state, print it in a human-readable way.

        :param blackboard: Blackboard with the current state of the problem
        :param additional_information: Additional information for the node to store in the blackboard
        :return: The specified result
        """
        blackboard.set_in_states(
            self.__id,
            {NODE_RESULT: ResultEnum.RUNNING, ADDITIONAL_INFORMATION: additional_information}
        )
        self.print_message("RUNNING")

        return ResultEnum.RUNNING

    def report_succeeded(self, blackboard: Blackboard, additional_information: Any = None):
        """
        Before returning the succeeded state, print it in a human-readable way.

        :param blackboard: Blackboard with the current state of the problem
        :param additional_information: Additional information for the node to store in the blackboard
        :return: The specified result
        """
        blackboard.set_in_states(
            self.__id,
            {NODE_RESULT: ResultEnum.SUCCEEDED, ADDITIONAL_INFORMATION: additional_information}
        )
        self.print_message("SUCCEEDED")

        return ResultEnum.SUCCEEDED

    def result(self, blackboard: Blackboard) -> ResultEnum:
        """
        Find the result of the node in the specified blackboard.

        :param blackboard: Blackboard with the current state of the tree
        :return: Result of this node or None if not found
        """
        if not blackboard.is_in_states(self.__id):
            return ResultEnum.UNDEFINED
        return blackboard.get_in_states(self.__id)[NODE_RESULT]

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        return self.report_failed(blackboard)
