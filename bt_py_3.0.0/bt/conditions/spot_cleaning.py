#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import bt as bt
from ..globals import SPOT_CLEANING


class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "battery_level < 30".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Cleaning Spot')
        # bt.Timer(10, bt.FindHome())
        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, False) \
            else self.report_failed(blackboard)
