#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from enum import Enum

# Definition of some common types
EnvironmentKeyType = str
NodeIdType = int


# Possible results of an evaluation
class ResultEnum(Enum):
    UNDEFINED = 0
    FAILED = 1
    RUNNING = 2
    SUCCEEDED = 3


# State information keys
ADDITIONAL_INFORMATION = 'additional_information'
NODE_RESULT = 'result'
RUNNING_CHILD = 'running_child'
