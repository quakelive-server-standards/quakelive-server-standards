All fields should be present and of the correct type.

"id" is how you will refer to the factory inside a map pool or a callvote, and must be a string.
"title", "author" and "description" are all strings containing info about the factory, and can be seen in Start Match
"basegt" is a string of the base gametype it should apply the settings on. Valid values for "basegt" are:
ffa, duel, race, tdm, ca, ctf, oneflag, har, ft, dom, ad, rr
"cvars" is an object containing key value pairs of the cvar names and values to set.

If a factory is invalid, the reason why will be printed in the console during startup, and the factory will not be available for play.