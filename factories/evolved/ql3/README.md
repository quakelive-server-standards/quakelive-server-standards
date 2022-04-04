# QL3 - QL influenced by Q3

This is a very gentle convergence of Quake 3 and Quake Live. Only two variables are adjusted: `g_weaponrespawn` and `timelimit`.

Weapon respawn is changed to 15 seconds to enable weapon denying tactics. The time limit was slightly increased to 12 minutes because it is not seldomly that a control is broken after 7 minutes which leaves too little time left to win. 12 minutes should lead to more thoughtful play instead of overly aggressive rushing.

Weapon configurations are left QL'ish for now. In Q3 you had 100 rail, more splash radius rockets and a much stronger shaft. Since people aim a lot better these days, the adjustments made to the damage somewhat reflects that. Otherwise, overpowered weapons might be seen as a gameplay element. They might work if there is less ammunition available. The problem with Quake Live in that regard is, that you get an additional full amount of starting ammunition when recollecting a weapon while in Quake 3 you would get only 1 additinal ammunition item. Because of this, a player has a lot more ammunition and can create a lot more pressure than in Q3. In QL there is a lot less room to breathe. If you want to break out you have to hit something. It might be a matter of taste. For now we go with the aggressive QL style of play but add the possibility to deny weapons and therefor new ammunition also. This will force the player to shoot less or to go for new ammunition for which she/he might leave the good position which creates opportunities for the opponent. 

Other things like the shotgun spread, which is different in Q3, are irreparabel. But there are even more things like jump height or double jump, which does not exist in Q3.

Let us see were the journey leads us to. There is room to experiment. We should see this approach of evolving the QL formular with Q3 elements. Back to the roots a little but in the end it will not be possible to mirror Q3. This version will be an evolved Quake Live. Quake Live 3.

## Changed cvars

##### Timelimit

`timelimit "12"` - Timelimit of 12 minutes.

More of a Quake3'ish timelimit. It gives a better chance to come back which with 10 minutes timelimit most of the time is too little time.

##### Weapon respawn time

`g_weaponrespawn "15"` - Weapon respawn time of 15 seconds.

Quake 3 weapon respawn times to allow for weapon denying tactics. It will also reduce the amount of ammunition of the opponent and should lead to less offensive play.