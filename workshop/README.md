# Steam Workshop items

The [Steam Workshop for Quake Live](https://steamcommunity.com/app/282440/workshop/) is a place where you can upload and download free content for Quake Live. It contains mostly maps but also other things like the long absence [gibs](https://steamcommunity.com/sharedfiles/filedetails/?id=691078677) or [different media files](https://github.com/quakelive-server-standards/server-standards/blob/master/workshop/Minqlx_related.md) for certain minqlx plugins.

## Add Workshop items to a Quake Live dedicated server

A Steam Workshop item is added to a Quake Live dedicated server through a file called `workshop.txt`. Each line contains one Workshop item id.

```
691078677
539421606
```

You obtain such an id from the Steam Workshop item URL like this one `https://steamcommunity.com/sharedfiles/filedetails/?id=691078677` by copying the number from the id URL parameter `id=691078677`.

## Workshop item lists

- [Duel maps](https://github.com/quakelive-server-standards/server-standards/blob/master/workshop/Duel_maps.md)
- [Minqlx](https://github.com/quakelive-server-standards/server-standards/blob/master/workshop/Minqlx.md)
- [Other](https://github.com/quakelive-server-standards/server-standards/blob/master/workshop/Other.md)

## Download a Workshop item

You can download a Steam Workshop item for inspection before you deploy it to your Quake Live dedicated servers. Use the contained `download.sh` shell script to do so.

```
./download.sh 691078677
```

You will find the downloaded Steam Workshop item inside the `_items` directory. It will be a new directory which name is the Steam Workshop item id. Inside of it you will find the belonging files.

## Upload a Workshop item

## Convert a Quake 3 map to a Quake Live map

## Participate