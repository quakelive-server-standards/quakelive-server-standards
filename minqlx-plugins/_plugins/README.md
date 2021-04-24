# minqlx plugin overview

## minqlx

`mino/plugin_manager.py` - Adds commands to load, reload and unload plugins at run-time.
`mino/docs.py` -  A plugin that generates a command list of all the plugins currently loaded, in the form of a Markdown file.
`mino/raw.py` -  Adds commands to interact with the Python interpreter directly. Useful for debugging.

## Server

`mino/log.py` - A plugin that logs chat and commands. All logs go to `fs_homepath/chatlogs`.
`barelymissed/echo.py` - This plugin prints the command issuer and the command with arguments to the console so they can be seen and logged.
`mino/workshop.py` - A plugin that allows the use of custom workshop items that the server might not reference by default, and thus not have the client download them automatically.
`barelymissed/players_db.py` - This will save permissions on the server to a text file so the file can be moved to another server and loaded onto that database.
`barelymissed/restartserver.py` - Restart the server at a certain time, or as soon as the server empties, once the restart time has passed.
`barelymissed/getmap.py` - It allows the admin to download a map to the server and add new IDs to the server's workshop text file. It will them restart the server, if it is empty, so that the map can be played. It will also allow removal of maps from the server.
`em92-dynamicip/dynamicip.py` - Dynamicip is minqlx-plugin that will automaticly update your server address on qlstats.net admin panel before game starts. Useful for hosts with dynamic ip.
`cstewart90/servers.py` - Adds !servers command which shows info for a list of servers.

## Admin

`mino/essentials.py` - Adds commands for the regular QLDS commands and some more. Adds functionality to restrict teamsize voting and to pass votes before it fails if the majority votes yes.
`iouonegirl/myessentials.py` - Use names with the essential commands, like !red iou, !mute iou, !kick iou, ...
`mino/permission.py` - Adds commands to set player permissions.
`mino/ban.py` - Adds command to ban people for a set amount of time. Also adds functionality to ban for automatically for leaving too many games.
`mino/silence.py` - Adds commands to mute a player for an extended period of time. This persists reconnects, as opposed to the default mute behavior of QLDS.
`x0rnn/checkplayers.py` - A plugin to list all players with permission >= 1, banned, leaver-banned, leaver-warned and silenced players.
`cstewart90/checkplayers.py` - Based on x0rnns's checkplayers. Completely rewritten to use scan_iter instead of keys, and changed output to be a table. Also fixes IRC flooding and player getting disconnected with large outputs.
`barelymissed/specall.py` - When the time to start picking teams arrives it can be hard to get everyone to go to spectator so the process can start. This script will put everyone to spectate wth a single command. If the command is followed by a teamsize, the teamsize will be set to the desired size when everyone is put to spectator.
`barelymissed/protect.py` - I created this plugin to allow server admins to put people on a list that would not allow them to be kicked from a server.
`x0rnn/warn.py` - A plugin to warn players for misbehaving. A warning is removed after X days (qlx_warnDays), unless the player has been warned X times (qlx_maxStrikes), then he is perma-banned.
`barelymissed/voteban.py` - Add people to a vote ban list that would keep them from being able to vote on the server at all. The vote ban is set with an expiration time, set a long time if you want it to be effectively permanent.
`cstewart90/banvote.py` - Adds !banvote command to ban people from voting.
`iouonegirl/myban.py` - Use the !ban command with a player's name instead of ID.
`barelymissed/commands.py` - This script lists the loaded plugins and the commands available for each plugin.

## Players

`mino/clan.py` - Adds commands to let players have persistent clan tags without having to change the name on Steam.
`mino/names.py` - Adds a command to change names without relying on Steam.
`barelymissed/clanmembers.py` - This script was added to help admins manage who wears their clan's tag.
`x0rnn/titlerank.py` - Gives a player a title rank of: Admin, VIP, Regular, Member, Dork.
`x0rnn/specs.py` - To list players spectating you and to check who someone is spectating.
`roasticle/ragespec.py` - !ragespec to...ragespec!
`x0rnn/referee.py` - Gives referee status to a player with the password or one that has been callvoted (if enabled) and enables the following commands.
`roasticle/qltv.py` - Automatically spec the top player.
`iouonegirl/playerinfo.py` - Display some player information. Maybe upon player connect if you want. (Also gives a warning or a ban for deactivated qlstats accounts).
`barelymissed/inviteonly.py` - Will allow an admin to add people to the invite only list which allows them to play on the server.
`barelymissed/highping.py` - Check players when they join a team for a ping that is higher than the setting. Put the players back to spec who do not meet the ping requirements. Allow admins to execute the high ping check on all players using the !999 command.
`iouonegirl/afk.py` - Detect AFK people and place them in spectator (after a warning).
`mgaertne/afk_auto_spec.py` - Put players to spec during warmup.
`x0rnn/spec999.py` - Put players with 999 ping to spectator mode.
`roasticle/idlespec.py` - Puts a player who idles into spec instead of kicking her/him.
`mgaertne/elocheck.py` - Checks qlstats for the elos of a player given as well as checking the elos of potentially aliases of the player by looking for connection from the same IP as the player has connected to locally.
`barelymissed/databaseElo.py` - Store player ELOs on the server in the event qlstats goes down.
`mgaertne/qlstats_privacy_policy.py` - Plugin that restricts playing on the server to certain QLStats.net privacy settings.

## Bots

`barelymissed/bots.py` - This is a plugin for the minqlx admin bot. This keeps the server populated with bots (up to the set number) and will kick a bot to replace with a human player when they join. This is intended to give people a place to play even when no one else is playing.
`barelymissed/restartonlybots.py` - It kicks bots out of a server if they are the only ones remaining.
`roasticle/bot_antispec.py` - Kicks bots that are spectators.
`x0rnn/addbot.py` - Lets a player add a single nightmare bot into the game with either a 0, 60 or 200 millisecond thinktime (smaller is stronger).

## Teams

`barelymissed/teamsize.py` - Limit the teamsize admins are able to set when using !teamsize or !ts.
`barelymissed/handicap.py` - Handicap people who join the server based on their ELO. That means you could uncap your server and just have it auto handicap people as they join. It will not let the client change their handicap without admin permission.
`iouonegirl/anti_rape.py` - In round-based game modes; apply calculated handicaps to people playing above the server average.
`mattized/uneventeams.py` - This plugin takes care of uneven teams. If uneven teams occur this plugin finds the player who has played the least amount of time since he connected.
`barelymissed/serverBDM.py` - This script collects data on the players on the server and calculates a Basic Damage Metric (BDM) rating. It works for game types Clan Arena, Freeze Tag, Free For All, Capture The Flag, Instagib Capture the Flag, and Team Death Match. The script will do balancing and switch recommendations.
`iouonegirl/autospec.py` - If CA or FT teams are uneven, make the last person spec.
`mgaertne/auto_rebalance.py` - This plugin automatically rebalances new-joiners at round start based upon the ratings in the balance plugin.
`iouonegirl/mybalance.py` - Elo-limits, warmup reminders, team balancing for CA, TDM, CTF, FT.
`mgaertne/merciful_elo_limit.py` - Gives players below a specified elo minimum the chance to play a certain amount of application games.
`mattized/queue.py` - Implements duel-like queue into the all gametypes. Players receive a status, which is  displayed in a round brackets: (s) - spectating, (1..2..n) - position in queue, (AFK) - afk status. For team-based gametypes plugin waits for 2 players before adding them into the game in progress. Also players will be added to queue if there is no place in game (due teamsize or locked teams).
`barelymissed/specqueue.py` - This plugin is intended to help keep the game as enjoyable as possible, without the hassles of people making teams uneven, or someone joining later than others, but happening to hit the join button first and cutting in line when a play spot opens.

## Voting

`mino/balance.py` - Adds commands and cvars to help balance teams in team games using ratings provided by third-party services.
`barelymissed/doVote.py` - Allow players to callvote forcing the suggested player switch gotten from !teams.
`barelymissed/voicechat.py` - This script allows players to be able to vote for global or team voice chat setting g_alltalk.
`barelymissed/votelimiter.py` - Keep people from callvoting stupid votes and votes that mess up the server but the admin hadn't thought about.
`iouonegirl/disable_votes.py` - Disable the ability to make certain callvotes during a game.
`mgaertne/custom_modes_vote.py` - This plugin allows switching to customizable game modes, ships with vanilla QL settings and PQL promode settings.
`mgaertne/fastvotes.py` - This plugin modifies the default vote pass or fail behavior with customizeable logic.
`x0rnn/vote.py` - A plugin to call the following custom votes: mode, weaponrespawn, thrufloors, footsteps, ...
`roasticle/funstuff.py` - Various fun vote functions.
`iouonegirl/specprotect.py` - This plugin protects spectators from being targeted by kick callvotes.

## Game types

`mino/solorace.py` - A plugin that starts the game and keeps it running on a race server without requiring a minimum of two players, like you usually do with race.
`barelymissed/battleroyal.py` - This is a plugin for the minqlx admin bot. It makes a last man standing game style played in FFA with some default weapons.
`barelymissed/wipeout.py` - This adds a gametype to QL that runs under the Clan Arena mode. To win a round a team has to have the entire enemy team dead at the same time. When a player dies they remain in spectate for a period of time before respawning. The time in spectate increases with each team mate death, so as the round progresses it becomes more likely that the entire enemy team can be dead at the same time.
`barelymissed/funwarmup.py` - It modifies the game CVARs to make warmup time a little different and hopefully more fun.
`em92-ad_hacks/minqlx-plugins/swap_bases_ad.py` - Plugin to make some non-symmetrical maps playable in A&D gamemode.
`mgaertne/duelarena.py` - Round winner stays in, loser rotates with spectator. For CA.
`cstewart90/removepowerups.py` - Removes powerups on round end. Mainly used for freezetag because `g_freezeRemovePowerupsOnRound` doesn't remove powerups right away.
`em92-kamikaze-clanarena` - Kamikaze Clan Arena is modification of Clan Arena gamemode which enables players to use kamikaze. Item spawns in 10 seconds after round stars.
`roasticle/gungames.py` - Custom voting triggers for gungames factories.
`iouonegirl/sets.py` - This plugin allows two players to duel a certain amount of games in succession without being interrupted by other players.
`iouonegirl/gauntonly.py` - When 1 last standing person faces a lot of enemies, start gauntonly mode.
`x0rnn/midair_only.py` - This plugin changes the gameplay into a rockets-only mode where only midair shots kill.
`x0rnn/fastrespawn.py` - If you selfkill, you respawn in 1.8 seconds like in Q3 instead of waiting 3 seconds (QL default).
`roasticle/weaponspawnfixer.py` - Override map-forced weapon spawn times.

## Stats

`barelymissed/kills.py` - This script is meant to give the players a little more fun by having some extra goals to try for in the game.
`mattized/pummel.py` - It displays "Killer x:y Victim" message when Victim gets killed with gauntlet and stores the information in REDIS DB
`x0rnn/stats.py` - Show some simple kill stats: kills, deaths, k/d ratio, kills per minute.
`x0rnn/scores.py` - Shows player/team info such as kills, deaths, damage given, damage received, elos, average team elo, etc.
`x0rnn/midair.py` - A plugin that keeps score of top X midair rocket kills per map in terms of distance.
`mgaertne/frag_stats.py` - ?
`roasticle/uberstats.py` - Various awards and stats added during and endgame.

## Maps

`barelymissed/listmaps.py` - This script lists all the maps loaded on the server.
`barelymissed/mapLimiter.py` - I created this script to limit the maps that can be voted for on a server.
`barelymissed/mapmonitor.py` - If the server boots everyone due to a bad map it will change the map to the default map. It can also monitor for the server emptying out and change to the default map.
`em92-ad_hacks/minqlx-plugins/map_config.py` - Loads config file depending on running map.
`roasticle/gravityfixer.py` - restores gravity to normal after maps with custom gravity
`roasticle/nextmap.py` - Announce nextmap and fix nextmap repeats.
`roasticle/mapoo.py` - Allows multiple mappool files that change automatically based on player number.

## Messages

`mino/motd.py` - Adds commands to set a message of the day.
`iouonegirl/centerprint.py` - Provides easy way to broadcast messages on peoples screens, and provides a "last enemy standing" toggle.
`iouonegirl/railable.py` - Toggle to get a 'railable' message when your health drops too low.
`mgaertne/thirtysecwarn.py` - A minqlx plugin to play unused VO when a CA game is nearing the round time limit.
`roasticle/motd.py` - A replacement motd plugin that allows multiple motd/welcome sounds.

## Chat

`mino/irc.py` - Has a small built-in IRC client that can relay chat to and from an IRC channel. It can also be used to remotely execute minqlx commands.
`iouonegirl/myirc.py` - Supports broadcasting to keyed (passworded) channels, shows more colors, and broadcasts live updates to the topic.
`mgaertne/mydiscordbot.py` - The plugin's main purpose is to create a relay chat between the Quake Live chat and configured discord channels.
`roasticle/discordbot.py` - Announce server stats to your Discord server!
`x0rnn/english.py` - English motherfucker, do you speak it?
`x0rnn/urltitle.py` - Prints the title of a website/youtube link, etc. posted in chat.
`x0rnn/tts.py` - Primitive TTS (text-to-speech) system based on arpabet.
`mino/extras/textart.py` - Converts links to images pasted in chat to the same image, but represented in unicode. 

## Sounds

`barelymissed/chatfun/chatfun.py` - Allow the server to respond to things said in the server.
`barelymissed/myfun/myFun.py` - This is my replacement for the minqlx fun.py so if you use this file make sure not to load fun.py. This plugin plays sounds for players on the Quake Live server. It plays the sounds included in fun.py and some from other workshop item sound packs.
`iouonegirl/funlimit.py` - Automatically disables fun(.py) sounds during a match/rounds.
`mino/fun.py` - Plays sounds on certain words typed in chat.
`ped-ro/westcoastcrew.py` - Plays sounds on certain words typed in chat.
`roasticle/crash.py` - !crash for random crash noob intro sounds :D
`roasticle/duke.py` - Duke Nukem sound triggers.
`roasticle/fun.py` - Plays sounds triggered by certain words typed in the chat.
`roasticle/intermissionplus.py` - Allow players to set custom victory songs.
`roasticle/winneranthem.py` - Plays anthem for winner's country at end of match!
`x0rnn/killingspres.py` - Unreal Tournament sound announcements.
`iouonegirl/intermission.py` - Play 1 song out of a list after every match end.

## Other

`iouonegirl/translate.py` - It provides commands to translate words and sentences, look up definitions, and much more.
`roasticle/weather.py` - Lets you check weather and forecast in-game!
`x0rnn/coinprice.py` - Shows current bitcoin/ethereum/litecoin price and info.
`roasticle/roasted.py` - Roasticles standards.
