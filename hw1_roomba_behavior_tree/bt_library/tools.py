#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from .blackboard import Blackboard
from .common import NODE_RESULT, ADDITIONAL_INFORMATION, ResultEnum, NodeIdType


def cancel_running(blackboard: Blackboard):
    """
    Cancel the running state of every node in the blackboard.

    :param blackboard: Blackboard with the current state to query
    """
    # First, find all the tree nodes in a RUNNING state. The blackboard cannot be modified
    # during the traversal
    running_nodes = []
    for node in blackboard.get_all_states():
        tree_node_id = NodeIdType(node[0])
        result = ResultEnum(node[1][NODE_RESULT])

        if result == ResultEnum.RUNNING:
            running_nodes.append(tree_node_id)

    # Remove all the found tree nodes
    for running_node_id in running_nodes:
        blackboard.remove_state(running_node_id)


def print_states(blackboard: Blackboard):
    """
    Print the state of every node in the blackboard.

    :param blackboard: Blackboard with the current state to query
    """
    for node in blackboard.get_all_states():
        tree_node_id = NodeIdType(node[0])
        result = ResultEnum(node[1][NODE_RESULT])
        additional_info = node[1][ADDITIONAL_INFORMATION]

        print(f'Tree node id: {tree_node_id}')
        print(f'Result: {result}')
        print(f'Additional information: {additional_info}')
