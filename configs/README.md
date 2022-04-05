# Quake Live server configurations

This directory contains variants of the `server.cfg` as it is intended to be used by the Quake Live Server Standards server framework. It contains technical and server framework specific cvars which are invariant to any specific server instance and any specific gametype. If you are looking to set values which are server instance or gametype specific, there are three other locations where your cvars should go into. Take a look [here](https://github.com/quakelive-server-standards/server-standards/tree/master/_myservers#configuring-your-quake-live-servers).

## Overview

### Standard

There is a standard `server.cfg` for all server configurations since it does not contain any server instance or game type specific settings. It also contains vital settings for the Docker-based server framework to function. You can read about the standardized values [here](https://github.com/quakelive-server-standards/server-standards/tree/master/configs/standard#readme).

### Evolved

No evolutions yet.

### id Software originals

The directory `_id` contains the original `server.cfg` along with the original `server_readme.txt`.

## Participe

### Contributing your `server.cfg`

Suppose you found a value for a technical cvar which helps running Quake Live servers more stable. You added it to your own `server.cfg`, which you have based on one of config files either in `configs/standard` or `configs/evolved`. Now you want to contribute that file back to the Quake Live Server Standards repository. Do the following steps.

1. Create a fresh clone of the official Quake Live Server Standards Git repository.
2. Create a new directory inside the `configs/evolved` directory. Name it as you like.
3. Put your `server.cfg` file into it.
4. Create a README.md file like the one in [`configs/evolved/_example/README.md`](https://github.com/quakelive-server-standards/server-standards/blob/master/configs/evolved/_example/README.md).
5. Create a Git commit and push it to the official Quake Live Server Standards repository. It will result in a merge request which the Quake Live Server Standards admins will process. It may be the case that they want you to change things. So keep an eye on your emails to not miss the corresponding notifications.

### Community Standard Passing Process

If you want to change the standard `server.cfg` file, follow these steps.

1. The cvars that you want to change need to be present in one of the `server.cfg` files of the `configs/evolved` directory. Either you refer to one which is already present or you at first need to contribute your own.
2. Create a GitHub issue and label it with `Standard discussion`.