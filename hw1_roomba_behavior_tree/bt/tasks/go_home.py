#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import HOME_PATH


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Going Home')

        # recall home path
        path = blackboard.get_in_environment(HOME_PATH, 'home not found')
        print(path)
        return self.report_succeeded(blackboard)
