#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - Copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from typing import Dict, Any, Optional, Iterable, Tuple

from .common import EnvironmentKeyType, NodeIdType


# Definition of the blackboard class
class Blackboard:
    """
    Class of the blackboard.
    """
    __environment: Dict[EnvironmentKeyType, Any]  # State of the environmental variables
    __states: Dict[NodeIdType, Any]  # State of the nodes

    def __init__(self):
        """
        Default constructor.
        """
        self.__states = dict()
        self.__environment = dict()

    def get_all_states(self) -> Iterable[Tuple[NodeIdType, Any]]:
        """
        Return all the node states stored in the blackboard.

        :return: The iterable set of tuples for the items in the node states
        """
        return self.__states.items()

    def get_in_environment(self, key: EnvironmentKeyType, default_value: Optional[Any]) -> Any:
        """
        Return the value in the environment associated with the specified key.

        :param key: Key to query
        :param default_value: Value to return if the node state was not found in the blackboard
        :return: The value associated with the key (if it exists)
        """
        return self.__environment[key] if key in self.__environment else default_value

    def get_in_states(self, node_id: NodeIdType) -> Any:
        """
        Return the value in the states associated with the specified node ID.

        :param node_id: Identification of the node to query
        :return: The value associated with the node ID (if it exists)
        """
        return self.__states[node_id] if node_id in self.__states else None

    def is_in_states(self, node_id: NodeIdType) -> bool:
        """
        Return TRUE if the specified node ID is in the states map.

        :param node_id: Identification of the node to query
        :return: TRUE if the node ID is in the states map
        """
        return node_id in self.__states

    def remove_state(self, node_id: NodeIdType) -> None:
        """
        Remove the state of the specified node.

        :param node_id: Identification of the node to remove
        """
        self.__states.pop(node_id)

    def set_in_environment(self, key: EnvironmentKeyType, value: Any) -> None:
        """
        Set a variable in the environment portion of the blackboard.

        :param key: Key to set
        :param value: Value associated with the key
        """
        self.__environment[key] = value

    def set_in_states(self, node_id: NodeIdType, value: Any) -> None:
        """
        Set a variable in the states portion of the blackboard.

        :param node_id: Identification of the node to set
        :param value: Value associated with the key
        """
        self.__states[node_id] = value
