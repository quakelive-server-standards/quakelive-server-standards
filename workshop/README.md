# Steam Workshop items

The [Steam Workshop for Quake Live](https://steamcommunity.com/app/282440/workshop/) is a place where you can upload and download free content for Quake Live. It contains mostly maps but also other things like the long absence [gibs](https://steamcommunity.com/sharedfiles/filedetails/?id=691078677) or [different media files](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/workshop/evolved/minqlx) for certain minqlx plugins.

## Add Workshop items to a Quake Live dedicated server

A Steam Workshop item is added to a Quake Live dedicated server through a file called `workshop.txt`. Each line contains one Workshop item id.

```
691078677
539421606
```

You obtain such an id from the Steam Workshop item URL like this one `https://steamcommunity.com/sharedfiles/filedetails/?id=691078677` by copying the number from the id URL parameter `id=691078677`.

## Download a Workshop item

You can download a Steam Workshop item for inspection before you deploy it to your Quake Live dedicated servers. Use the contained `download.sh` shell script to do so.

```
./download.sh 691078677
```

You will find the downloaded Steam Workshop item inside the `_items` directory. It will be a new directory which name is the Steam Workshop item id. Inside of it you will find the belonging files.

In an improved version, the script would also extract the contained `*.pk3` files. This is not implemented yet. If you would know how to add that feature, take a look into this [GitHub issue](https://github.com/quakelive-server-standards/quakelive-server-standards/issues/20).

## Upload a Workshop item

This is still work in progress. If you know how to do it, take a look into this [GitHub issue](https://github.com/quakelive-server-standards/quakelive-server-standards/issues/22).

## Convert a Quake 3 map to a Quake Live map

This feature was not added yet. If you have an idea on how to do it, take a look at this [GitHub issue](https://github.com/quakelive-server-standards/quakelive-server-standards/issues/18).

## Evolve Quake Live