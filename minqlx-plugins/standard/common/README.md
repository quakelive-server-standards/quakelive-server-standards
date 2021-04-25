# minqlx common plugins

##### Balance

`balance.py` - Adds commands and cvars to help balance teams in team games using ratings provided by third-party services.

This plugin contains the popular `!elos` command which players expect to be supported.

##### Commands

`commands.py` - This script lists the loaded plugins and the commands available for each plugin.

Minqlx plugins are one of the most effective ways of evolving Quake Live. Plugins expose their functionality through commands which are typed into the Quake Live console. Players need to know these commands and how they work. This plugin prints out an overview over every command that is installed.

##### Docs

`docs.py` - A plugin that generates a command list of all the plugins currently loaded, in the form of a Markdown file.

Might be useful for a server admin to have an overview over his servers or to present command lists publically to the players.

##### Essentials

`essentials.py` - Adds commands for the regular QLDS commands and some more.

It extends the built-in Quake Live commands and adds useful tools to facilitate the minqlx features.

##### List maps

`listmaps.py` - This script lists all the maps loaded on the server.

The Quake Live built-in map voting menu does not reflect the defined map pool and the maps are not sorted alphatically. Thus this plugin complements custom map pools and gives the players the possibility to get an overview of the available maps in the console.

##### Log

`log.py` - A plugin that logs chat and commands. All logs go to fs_homepath/chatlogs.

It provides a certain very basic logging facility.

##### Permission

`permission.py` - Adds commands to set player permissions.

It enables to give players minqlx permission levels. It is a basic tool when working for a server admin.

##### Plugin manager

`plugin_manager.py` - Adds commands to load, reload and unload plugins at run-time.

It provides fundamental functionality for the work with minqlx.
