# Quake Live server configurations

This directory contains variants of the `server.cfg` as it is intended to be used by Quake Live Server Standards. It contains technical and Quake Live server framework specific cvars. If you are looking to set values regarding other topics, there are three additional locations for cvars, which are command line parameters, in the `autoexec.cfg` and inside a `*.factories` file. Take a look into this [README.md](https://github.com/quakelive-server-standards/server-standards/tree/master/_myservers#configuring-your-quake-live-servers) of the `_myservers` directory for an explanation.

## Overview

### Standard

There is a standard `server.cfg` for all server configurations since it does not contain any game type specific settings. It also contains vital settings for the Docker-based server framework to function. You can read about the standardized values [here](https://github.com/quakelive-server-standards/server-standards/tree/master/configs/standard#readme).

### Evolved

No evolutions yet.

### id Software originals

The directory `_id` contains the original `server.cfg` along with the original `server_readme.txt`.

## Participating

### Contributing your `server.cfg`

Suppose you found a value for a technical cvar which helps running Quake Live servers more stable. You added it to your own `server.cfg`, which you have based on the standard config file in `standard/server.cfg`. Now you want to contribute that file back to the Quake Live Server Standards repository. Do the following steps.

1. Create a fresh clone of the official Quake Live Server Standards Git repository.
2. Create a new directory inside the `configs/evolved` directory. Name it as you like.
3. Put your `server.cfg` file into it.
4. Create a README.md file like the one in `configs/evolved/_example/README.md`.
5. Create a Git commit and push it to the official Quake Live Server Standards repository. It will result in a merge request which the Quake Live Server Standards admins will process. It may be the case that they want you to change things. So keep an eye on your emails to not miss the corresponding notifications.

### Community Standard Passing Process

If you want to change the standard `server.cfg` file, follow these steps.

1. The cvars that you want to change need to be present in one of the `server.cfg` files of the `configs/evolved` directory. Either you refer to one which is already present or you at first need to contribute your own.
2. Create a GitHub issue and label it with `Standard discussion`.