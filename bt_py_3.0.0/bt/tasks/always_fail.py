#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import CHARGING, BATTERY_LEVEL


class AlwaysFail(btl.Task):
    """
    Implementation of the Task "Always Fail".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Failed')
        return self.report_failed(blackboard)
