#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import CHARGING, BATTERY_LEVEL


class Charge(btl.Task):
    """
    if battery 100, stop charging. if not, keep running. what actually changes the battery level is in main
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Charging')

        # blackboard.set_in_environment(CHARGING, True)
        if blackboard.get_in_environment(BATTERY_LEVEL, 0) == 100:
            blackboard.set_in_environment(CHARGING, False)
            return self.report_succeeded(blackboard)
        else:
            blackboard.set_in_environment(CHARGING, True)
            return self.report_running(blackboard)
        # blackboard.set_in_environment(CHARGING, False)
        # return self.report_succeeded(blackboard)
