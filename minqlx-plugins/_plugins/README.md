# minqlx plugin overview

## minqlx

##### mino/plugin_manager.py

Adds commands to load, reload and unload plugins at run-time.

##### mino/docs.py

##### mino/raw.py

## Server

##### mino/irc.py

##### mino/log.py

##### mino/motd.py

##### mino/workshop.py

## Players

##### mino/ban.py

##### mino/clan.py

##### mino/irc.py

##### mino/permission.py

##### mino/names.py

##### mino/silence.py

##### barelymissed/clanmembers.py

This script was added to help admins manage who wears their clan's tag. This works with players trying to set their tag on the server using the !clan command. The protected tags can be stored as you want them to appear when you are listing the protected tags, so store them with colors and case settings of your choice.

## Voting

##### mino/balance.py

##### mino/essentials.py

## Teams

##### mino/essentials.py

## Game types

##### mino/solorace.py

##### barelymissed/battleroyal.py

This is a plugin for the minqlx admin bot. It makes a last man standing game style played in FFA with some default weapons.

##### barelymissed/wipeout.py

This adds a gametype to QL that runs under the Clan Arena mode. To win a round a team has to have the entire enemy team dead at the same time. When a player dies they remain in spectate for a period of time before respawning. The time in spectate increases with each team mate death, so as the round progresses it becomes more likely that the entire enemy team can be dead at the same time.

## Sounds

##### barelymissed/chatfun/chatfun.py

Allow the server to respond to things said in the server.

##### barelymissed/myfun/myFun.py

This is my replacement for the minqlx fun.py so if you use this file make sure not to load fun.py. This plugin plays sounds for players on the Quake Live server. It plays the sounds included in fun.py and some from other workshop item sound packs.

##### barelymissed/bots.py

This is a plugin for the minqlx admin bot. This keeps the server populated with bots (up to the set number) and will kick a bot to replace with a human player when they join. This is intended to give people a place to play even when no one else is playing.

##### barelymissed/commands.py

This script lists the loaded plugins and the commands available for each plugin.

##### barelymissed/databaseElo.py

Store player ELOs on the server in the event qlstats goes down.

##### barelymissed/doVote.py

Allow players to callvote forcing the suggested player switch gotten from !teams.

##### barelymissed/echo.py

This plugin prints the command issuer and the command with arguments to the console so they can be seen and logged.

##### barelymissed/funwarmup.py

It modifies the game CVARs to make warmup time a little different and hopefully more fun.

##### barelymissed/getmap.py

It allows the admin to download a map to the server and add new IDs to the server's workshop text file. It will them restart the server, if it is empty, so that the map can be played. It will also allow removal of maps from the server. This wills imply comment the ID in the workshop file then restart the server. This has worked in my tests every time. I am not guaranteeing it will work in every case.

##### barelymissed/handicap.py

Handicap people who join the server based on their ELO. That means you could uncap your server and just have it auto handicap people as they join. It will not let the client change their handicap without admin permission.

##### barelymissed/highping.py

Check players when they join a team for a ping that is higher than the setting. Put the players back to spec who do not meet the ping requirements. Allow admins to execute the high ping  check on all players using the !999 command.

##### barelymissed/inviteonly.py

Aallow you to have an invite only server that wouldn't reply on passwords that can be given to anyone. The inviteonly.py script will allow an admin to add people to the invite only list which allows them to play on the server.

Anyone not on the invite only list will be kicked from the server or confined to spectator, depending on the script settings.

Players can be allowed to spectate for a settable amount of minutes (default is 3) to allow a server admin to easily add them to the invite only list with the connected player's client id (goten from the !id command or the /players command). 

The script can also be set to kick people not on the invite only list as soon as they connect to the server. The permission level needed to admin the invite only list is settable. See the CVAR section below for instructions.

##### barelymissed/kills.py

This script is meant to give the players a little more fun by having some extra goals to try for in the game.
It records any pummel/gauntlet kill, any direct grenade kill, any air rocket, and any air plasma kill. It records who you
killed and how any times you have killed that person and displays the ratio of your kills to your victims kills on you.

You can look at each of the recorded types of kills with the commands !pummel, !grenades, !rockets, !plasma.
These commands will show you a total kill amount you have for each kind of kill and your kill ratio against
any player connected to the server at the time.

There are also end of the match stats posted when the map ends. These stats are per-map stats, not lifetime stats like
the stats gotten with the above commands.

##### barelymissed/listmaps.py

I created this script to be able to list all the maps loaded on the server.

This script creates a map list when the server starts, the plugin is reloaded, or the admin enters the '!getmaps' command.
The people on the server are able to use the '!listmaps' command to see all the maps loaded on the server.

##### barelymissed/mapLimiter.py

I created this script to limit the maps that can be voted for on a server. It does the same type of thing that
setting qlx_enforceMappool '1'. 

By default the maps in the baseq3/mappool.txt will be used. Set the qlx_mapLimiterFile cvar to point to a different file.

Lists the maps available for play on the server.

##### barelymissed/mapmonitor.py

This is a script to monitor the server when a map changes. If the server boots everyone due to a bad map it will change the map to the default map. It can also monitor for the server emptying out and change to the default map.

##### barelymissed/players_db.py

This will save permissions on the server to a text file so the file can be moved to another server and loaded onto that database.

##### barelymissed/protect.py

I created this plugin to allow server admins to put people on a list that would not allow them to be kicked from a server.

I also added the ability to vote players to spectator if they are AFK. I added that because I didn't want someone who can't be kicked to go AFK and get stuck taking up a play slot because he/she can't be kicked. It is used by "/cv afk 'player id'" in the console.

I get tired of people being in the server that are just annoying with their chat messages or talking. I added the ability for people to callvote MUTE players on the server. It is used with "/cv mute 'player id'" in the console. To callvote to unmute someone use "/cv unmute 'plyer id'". A player can't callvote to unmute themselves.

The script also stops map voting once a match has gone active. Voting maps during warm-up still works. I wanted a way to still allow voting during a match but to not allow voting different maps throughout the match because one or two people didn't like the map.

Join messages about the map voting and the use of voting people to spectator are displayed to players upon connect to the server. These messages can be disabled seperately so both, either, or no messages will be sent upon connect.

I received requests to be able to set a teamsize to any size, even it the teamsize you want is lower than the current teamsize actually on each team. With the <i>!forcets</i> command you can do just that.

##### barelymissed/restartonlybots.py

It kicks bots out of a server if they are the only ones remaining.

##### barelymissed/restartserver.py

Restart the server at a certain time, or as soon as the server empties, once the restart time has passed.

##### barelymissed/serverBDM.py

This script collects data on the players on the server and calculates a Basic Damage Metric (BDM) rating. It works for game types Clan Arena, Freeze Tag, Free For All, Capture The Flag, Instagib Capture the Flag, and Team Death Match.

The script will do balancing and switch recommendations.

##### barelymissed/specall.py

This script was added to help admins running pickup games.

When the time to start picking teams arrives it can be hard to get everyone to go to spectator so the process can start. This script will put everyone to spectate wth a single command.

If the command is followed by a teamsize, the teamsize will be set to the desired size when everyone is put to spectator.

##### barelymissed/specqueue.py

This is a queueing plugin for the minqlx admin bot. This plugin can be used alone or with the serverBDM.py plugin.

This plugin is intended to help keep the game as enjoyable as possible, without the hassles of people making teams uneven, or someone joining later than others, but happening to hit the join button first and cutting in line when a play spot opens.

The plugin will also attempt to keep team games even, when adding 2 players at once, by putting players into the most appropriate team, based on team scores or player BDMs.

This plugin will spectate people when teams are uneven. It will, by default settings, first look at player times then player scores to determine who, on the team with more players, gets put to spectate. When a player gets put to spectate they will automatically get put into the queue at the beginning of the line.

There is also the option to have the players in spectate for too long (set with qlx_queueMaxSpecTime) to be kicked. This will only kick the player, not do any kind of ban, so the player can reconnect immediately. This feature will not kick people with permission levels at or above the qlx_queueAdmin level, or people who are in the queue.

Use the command '!fix' to fix a player that is shown as sarge and not seen as an enemy or a team mate. This will set each player's model the the model recorded when they joined the server.

Read the top of the file to know how to set the required cvars for your server once the default values are not desired. There are a lot of settings to help server admins set up the server to better admin the server how they desire.

##### barelymissed/teamsize.py

Limit the teamsize admins are able to set when using !teamsize or !ts.

##### barelymissed/voicechat.py

This script allows players to be able to vote for global or team voice chat setting g_alltalk.

##### barelymissed/voteban.py

Add people to a vote ban list that would keep them from being able to vote on the server at all. The vote ban is set with an expiration time, set a long time if you want it to be effectively permanent.

##### barelymissed/votelimiter.py

Keep people from callvoting stupid votes and votes that mess up the server but the admin hadn't thought about. This script will keep people from being able to callvote something that has not been added to the Allowed Vote List.

This will stop any vote type, if enabled, that is not in the allowed vote list. This will also count the amount of votes people make and will limit it to the valuer set with "qlx_votelimiterLimit".

Quake Live has an included vote limiting feature that works well until the map changes, like in a callvote (map), then the Quake Live vote count resets. This script will keep that count until a game/match ends.
