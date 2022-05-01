# Factory-focused cvar collection

This is a collection of cvars focused on defining factories.

You can find a complete pre-Steam area cvar reference here http://www.regurge.at/ql/ and post-Steam area supplements here
https://steamcommunity.com/sharedfiles/filedetails/?id=542672458.

This list is not complete. If you are good with cvars, take a look at this [GitHub issue](https://github.com/quakelive-server-standards/quakelive-server-standards/issues/19). It call for adding missing descriptions and more cvars.

## Voting

`g_allowVote "1"` - Allows voting to take place in a server.

`g_voteDelay "0"` - Delay allowing votes for X milliseconds after map load.

`g_voteLimit "0"` - Limit users to X votes per map.

`g_allowVoteMidGame "0"` - Allows voting to take place during a match.

`g_allowSpecVote "0"` - Allows spectators to call or cast votes in a server.

`g_voteFlags "0"` - Sets which vote commands are disabled on the server.

Add together the below values for which callvotes should be DISABLED e.g to disable map and nextmap 1+4=5.
map `1`, map_restart `2`, nextmap `4` (also hides the map list), gametype `8` (ex: "/callvote map campgrounds" will be allowed, but "/callvote map campgrounds ca" will fail), kick `16`, timelimit `32`, fraglimit `64`, shuffle `128`, teamsize `256`, cointoss/random `512`, loadouts `1024`, end-game voting `2048`, ammo (global) `4096`, timers (item) `8192`, weapon respawn `16382`

## Players

`sv_warmupReadyPercentage "0.51"` - Sets the minimum percentile of players of ready status required in a warm up match before the match starts.

`g_warmupDelay "15"` - Sets the amount of time (in seconds) it takes from progressing from warm up round to match start when enough players are ready to begin.

`g_warmupReadyDelay "0"` - Force the game to start after x seconds after someone readies up.

`g_warmupReadyDelayAction "1"` - Set to 1 to force players to spectator after g_warmupReady Delay, 2 to force ready up.

`g_inactivity "0"` - Sets the amount of time a player can be inactive for before being kicked from the server.

`g_timeoutLen "30"` - Sets the length of a timeout.

`g_timeoutCount "3"` - Sets the number of timeouts per player.

`g_alltalk "0"` - Voice Comms. `0` Limit voice comms to teams only during the match. `1` Allow all players to talk to each other.

## Round

`fraglimit`
`timelimit`
`g_overtime`
`scorelimit`
`g_suddenDeathRespawn`
`capturelimit`
`g_respawn_delay_max`
`g_respawn_delay_min`
`roundtimelimit`

## Team

`g_teamSizeMin`
`g_shuffle_automatic`

## Game modes

`g_instagib`
`g_rrDeathScorePenalty`
`g_rrInfected`
`g_vampiricDamage`
`g_quadHogIdle`
`g_quadHog`
`g_training`
`g_friendlyFire`

##### Team Deathmatch

##### Domination

`g_domCapTime`

##### CTF

`g_throwFlagVelocity`
`g_flagBounce`
`g_flagPhysics`

##### Freeze Tag

`g_freezeThawTime`
`g_freezeAutoThawTime`
`g_freezeEnvironmentalRespawnDelay`
`g_freezeRemovePowerupsOnRound`
`g_freezeResetArmorOnRound`
`g_freezeResetHealthOnRound`
`g_freezeResetWeaponsOnRound`
`g_freezeRoundDelay`
`g_freezeThawTick`
`g_freezeThawWinningTeam`

### Items

`g_spawnItemPowerup`
`g_runes`
`g_spawnItemHoldable`
`g_itemHeight`
`g_itemTimers`

##### Armor

`g_startingArmor`

##### Health

`g_spawnItemHealth`
`g_startingHealth`
`g_startingHealthBonus`

##### Ammo

`g_spawnItemAmmo`
`g_ammoRespawn`
`g_ammoPack`

##### Regeneration

`g_regenHealth`
`g_regenHealthRate`
`g_regenArmor`
`g_regenArmorRate`
`g_regenArmorAfterHealth`

##### Battle Suit

`g_battleSuitDampen`

### Movement

`g_speed`
`pmove_AirControl`
`pmove_BunnyHop`
`pmove_CrouchStepJump`
`pmove_JumpTimeDeltaMin`
`pmove_RampJumpScale`
`pmove_WaterSwimScale`
`pmove_WaterWadeScale`
`pmove_noPlayerClip`
`pmove_RampJump`
`pmove_WeaponRaiseTime`
`pmove_WeaponDropTime`
`pmove_StepHeight`
`pmove_CrouchSlide`
`pmove_AirAccel`

### Weapons

`g_infiniteAmmo`
`g_startingweapons`
`g_loadout`
`g_knockback_z` ?
`g_max_knockback` ?

##### Gauntlet

`g_knockback_g` 1
`g_damage_g` 50
`weapon_reload_gauntlet` 400

##### Machine Gun

`g_startingAmmo_mg` 100
`g_damage_mg` 5
`g_damage_mg_tdm` 4
`weapon_reload_mg` 100

##### Shotgun

`g_damage_sg` 5
`g_damage_sg_outer` 5
`g_knockback_sg` 1
`g_startingAmmo_sg`
`weapon_reload_sg` 1000
`cg_trueShotgun` ?

##### Grenade Launcher

`g_velocity_gl` 700
`g_damage_gl` 100
`g_splashdamage_gl` 100
`g_splashradius_gl` 150
`g_knockback_gl` 1.10
`weapon_reload_gl` 800
`g_startingAmmo_gl`

##### Lightning gun

`g_damage_lg` 7
`g_damage_lg_falloff` 1
`g_range_lg_falloff` 768
`g_knockback_lg` 1.50
`weapon_reload_lg` 50
`g_startingAmmo_lg`

##### HMG

`g_startingAmmo_hmg`
`disable_weapon_hmg`
`disable_ammo_hmg`

##### Rocket Launcher

`g_velocity_rl` 1000
`g_accelFactor_rl` 1
`g_accelRate_rl` 16
`g_damage_rl` 100
`g_splashdamage_rl` 84
`g_splashradius_rl` 120
`g_rocketsplashOffset` -10.0
`g_knockback_rl` 0.90
`g_knockback_rl_self` 1.10
`weapon_reload_rl` 800
`g_startingAmmo_rl`

##### Plasma Gun

`g_velocity_pg` 2000
`g_accelFactor_pg` 1
`g_accelRate_pg` 16
`g_damage_pg` 20
`g_splashdamage_pg` 15
`g_splashradius_pg` 20
`g_knockback_pg` 1.10
`g_knockback_pg_self` 1.30
`weapon_reload_pg` 100
`g_startingAmmo_pg`

##### Rail Gun

`g_damage_rg` 80
`g_knockback_rg` 0.85
`weapon_reload_rg` 1500
`g_startingAmmo_rg`

##### BFG

`g_velocity_bfg` 1800
`g_accelFactor_bfg` 1
`g_accelRate_bfg` 16
`g_damage_bfg` 100
`g_splashdamage_bfg` 100
`g_splashradius_bfg` 80
`g_knockback_bfg` 1
`weapon_reload_bfg` 300

#### Chain Gun

`g_damage_cg` 8
`g_knockback_cg` 1
`weapon_reload_cg` 50

#### Nail Gun

`g_nailbounce` 1
`g_nailbouncepercentage` 65
`g_nailcount` 10
`g_nailspeed` 1000
`g_nailspread` 400
`g_damage_ng` 12
`g_knockback_ng` 1
`weapon_reload_ng` 1000

#### Proxy Launcher

`g_damage_pl` 0
`g_splashdamage_pl` 100
`g_splashradius_pl` 150
`g_knockback_pl` 1
`weapon_reload_prox` 800
`g_proxMineTimeout` 20000

### Bots

`bot_dynamicSkill`
`bot_startingSkill`


### ?

`practiceflags`
`dmflags`
`g_allowkill`
`g_dropCmds`
`g_enemyLocators`
`g_forceDmgThroughSurface`
`g_complaintLimit`
`g_shufflePowerRatingThreshold`

`sv_includeCurrentMapInVote`
`g_teamForceBalance`
