#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
# from ..globals import HOME_PATH


class CleanSpot(btl.Task):
    """
    Implementation of the Task "Find Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Cleaning Dusty Spot')

        return self.report_succeeded(blackboard)
    '''QUESTION'''
    # should I put a timer in here?
