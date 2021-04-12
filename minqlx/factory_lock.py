# factory_lock.py - a minqlx plugin to lock gametype votes to specific factories.

"""
The following cvars are used on this plugin:
    qlx_factorysetLocked: Is used to prevent '/cv map mapname factory' votes. Default: 0
    qlx_factoryset: List of eligible factories for callvote. Default: 0
"""

import minqlx

class factory_lock(minqlx.Plugin):
    def __init__(self):
        self.add_hook("vote_called", self.handle_vote_called)

        self.set_cvar_once("qlx_factorysetLocked", "0")
        self.set_cvar_once("qlx_factoryset", "")
        
        self.plugin_version = "1.0"

    def handle_vote_called(self, caller, vote, args):
        if vote.lower() == "map" and self.get_cvar("qlx_factorysetLocked", bool):
            split_args = args.split()
            if len(split_args) < 2:
                return
            factory = split_args[1]
            allowed_factories = self.get_cvar("qlx_factoryset", str).split()
            if factory not in allowed_factories:
                caller.tell("Factory not allowed.  Choose from: %s" % (", ".join(allowed_factories)))
                return minqlx.RET_STOP_ALL