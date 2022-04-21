# Quake Live server configurations

This directory contains variants of the `server.cfg` as it is intended to be used by the Quake Live Server Standards server framework. It contains technical and server framework specific cvars which are invariant to any specific server instance and any specific gametype. If you are looking to set values which are server instance or gametype specific, there are three other locations where your cvars should go into. Take a look [here](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#configuring-your-quake-live-servers).

## Overview

### id Software originals

The directory `_id` contains the original `server.cfg` along with the original `server_readme.txt`.

### Standard

There is a standard `server.cfg` for all server configurations since it does not contain any server instance or game type specific settings. It also contains vital settings for the Docker-based server framework to function. You can read about the standardized values [here](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs/standard#readme).

### Evolved

Evolved `server.cfg` files which aim to improve the experience over the standard file. Cvars defined there might be voted upon to be included into the official Quake Live server standard.

## Evolve Quake Live

### Contributing an evolved `server.cfg`

Once you started adding cvars to your [`_myservers/autoexec.cfg`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/_myservers#autoexeccfg) it is possible that you find settings which help to improve the Quake Live experience for the players. If they fit into the category, appliecable to any Quake Live server instance disregarding the game type, create your own `server.cfg` and put your cvars into it. Before you start with an empty file, base your file  either on the [`standard`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs/standard) or on one of the [`evolutions`](https://github.com/quakelive-server-standards/quakelive-server-standards/tree/master/configs/evolved). In fact, this is a must. Evolved `server.cfg` files which do not base on an existing one will not be accepted.

Here are the instructions on how to contribute your file.

1. Use a fresh unaltered clone of the official Quake Live Server Standards Git repository.
2. Create a new directory inside the `configs/evolved` directory. Name it as you like.
3. Put your `server.cfg` file into it.
4. Create a README.md file like the one in [`configs/evolved/_example/README.md`](https://github.com/quakelive-server-standards/quakelive-server-standards/blob/master/configs/evolved/_example/README.md).
5. Create a Git commit and push it to the official Quake Live Server Standards repository. It will result in a merge request which the Quake Live Server Standards admins will process. It may be the case that they want you to change things. So keep an eye on your emails to not miss the corresponding notifications.

### Community Standard Passing Process

If you want to change the standard `server.cfg` file, follow these steps.

1. The cvars that you want to change need to be present in one of the `server.cfg` files of the `configs/evolved` directory. Either you refer to one which is already present or you at first need to contribute your own.
2. Create a GitHub issue and label it with `Standard discussion`.