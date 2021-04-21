import minqlx

class allowkill(minqlx.Plugin):
    def __init__(self):
        self.add_hook("map", self.handle_map)
        self.add_hook("game_start", self.handle_game_start)
        self.add_hook("game_end", self.handle_game_start)

    def handle_map(self, map_name, factory):
        self.set_cvar("g_allowKill", "1")

    def handle_game_start(self, data):
        self.set_cvar("g_allowKill", "0")

    def handle_game_end(self, data):
        self.set_cvar("g_allowKill", "1")