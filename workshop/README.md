# Quake Live Steam Workshop items

The Steam Workshop is a place where you can upload and download for free downloadable content for Quake Live. You can find it [here](https://steamcommunity.com/app/282440/workshop/).

## Download a Steam Workshop item

You can download a Steam Workshop item for inspection before you deploy it to your Quake Live dedicated servers. Use the contained `download.sh` shell script to do so.

```
./download.sh 691078677
```

You will find the downloaded Steam Workshop item inside the `_items` directory. It will be a new directory which name is the Steam Workshop item id. Inside of it you will find the belonging files.

## Converting Quake 3 maps to Quake Live

What about Q3 maps? Yet again, just grab the Q3 pk3 files and encode them for QL using qldec tool. When you're done just place them in local ql baseq3 folder. One bit of advice tho, when converting Q3 ctf maps, open them up in radiant and remove team arena content there and make sure the weapons are properly placed, because 3w map pack includes all the TA holdables + powerups by default to appear on the map. If you're a map maker you can also test your own maps directly on QL, no need to test it with cpma guys anymore.
