# This is a plugin created by iouonegirl(@gmail.com)
# Copyright (c) 2016 iouonegirl
# https://github.com/dsverdlo/minqlx-plugins
#
# You are free to modify this plugin to your custom,
# except for the version command related code.
#
# This plugin disables certain votes during a game
#
# Uses
# set qlx_disabled_votes_midgame "map"
# set qlx_disabled_specvotes_midgame "teamsize, kick, clientkick"
# set qlx_disabled_votes_permission "1"

import minqlx
import time
import os
import requests

VERSION = "v0.12"

# This code makes sure the required superclass is loaded automatically
try:
    from .iouonegirl import iouonegirlPlugin
except:
    try:
        abs_file_path = os.path.join(os.path.dirname(__file__), "iouonegirl.py")
        res = requests.get("http://wilma.vub.ac.be/~dsverdlo/minqlx-plugins/iouonegirl.py")
        if res.status_code != requests.codes.ok: raise
        with open(abs_file_path,"a+") as f: f.write(res.text)
        from .iouonegirl import iouonegirlPlugin
    except Exception as e :
        minqlx.CHAT_CHANNEL.reply("^1iouonegirl abstract plugin download failed^7: {}".format(e))
        raise

class disable_votes(iouonegirlPlugin):

    def __init__(self):
        super().__init__(self.__class__.__name__, VERSION)

        self.set_cvar_once("qlx_disabled_votes_midgame", "map")
        self.set_cvar_once("qlx_disabled_specvotes_midgame", "teamsize, kick, clientkick")
        self.set_cvar_once("qlx_disabled_votes_permission", "1")

        self.add_hook("vote_called", self.handle_vote)
        self.add_command(("disabled","disabled_votes"), self.cmd_disabled)

    def cmd_disabled(self, player, msg, channel):
        disabled_for_all = []
        for v in self.get_cvar("qlx_disabled_votes_midgame", set):
            disabled_for_all.append(v)

        disabled_for_spec = []
        for v in self.get_cvar("qlx_disabled_specvotes_midgame", set):
            disabled_for_spec.append(v)

        if disabled_for_all:
            m = "^7Unless perm ^6{}^7+, in-game votes for ^2{}^7 are disabled."
            m = m.format(self.get_cvar("qlx_disabled_votes_permission"), "^7, ^2".join(disabled_for_all))
            if disabled_for_spec:
                m += " Specs can also not vote for: ^2{}^7."
                m = m.format("^7, ^2".join(disabled_for_spec))

        elif disabled_for_spec:
            m = "Unless they have perm ^6{}^7+, specs can't vote for: ^2{}^7."
            m = m.format(self.get_cvar("qlx_disabled_votes_permission"), "^7, ^2".join(disabled_for_spec))
        else:
            m = "^7There are no callvotes that will be disabled during a match."

        channel.reply(m)


    def handle_vote(self, player, vote, args):

        if self.game.state != "in_progress": return

        if self.db.has_permission(player, self.get_cvar("qlx_disabled_votes_permission", int)):
            return # go ahead

        disabled_votes = []

        # These will always apply
        for v in self.get_cvar("qlx_disabled_votes_midgame", set):
            disabled_votes.append(v)

        # If spectator: extra restrictions
        if player.team == "spectator":
            for v in self.get_cvar("qlx_disabled_specvotes_midgame", set):
                disabled_votes.append(v)

        if vote in disabled_votes:
            player.tell('^1You are not allowed to callvote {} during a match!'.format(vote))
            return minqlx.RET_STOP_ALL




