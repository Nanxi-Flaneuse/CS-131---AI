#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from numpy.random import choice
# from ..globals import HOME_PATH


class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Cleaning the floor')

        if choice([True, False], 1, p = [0.85, 0.15])[0]:
            return self.report_succeeded(blackboard)
        return self.report_failed(blackboard)
