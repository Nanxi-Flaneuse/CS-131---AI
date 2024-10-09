#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import bt as bt
from ..globals import DUSTY_SPOT_SENSOR


class DustySpot(btl.Condition):
    """
    Implementation of the condition "DustySpot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False) \
            else self.report_failed(blackboard)
