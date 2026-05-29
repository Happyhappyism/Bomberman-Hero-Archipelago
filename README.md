# Setup Guide

## What you need
- Bizhawk https://tasvideos.org/BizHawk/ReleaseHistory#Bizhawk210
- The latest Bomberman Hero .apworld provided in the latest release post
https://discord.com/channels/731205301247803413/1330612852867858505/1330734687798300764


## Installation
Same as every other unsupported N64 apworld, 
- simply move bomberman_hero.apworld into the custom_worlds directory in your Archipelago install server
(default path: C:\ProgramData\Archipelago\custom_worlds)
- or simply double click the apworld and it should install itself (Archipelago version 0.5.0 and later)

## Running
1. In the Archipelago launcher push the 'Generate Template Options' button to generate a yaml for your options
2. Like every other apworld, fill out your yaml options and have the host generate the multiworld, the produced zip file should contain a .apbombh patch file. Recieve this .apbombh patch from the multiworld host.
3. Push the 'Open Patch' button in the launcher and it should ask for a 'Bomberman Hero (US)' legal ROM dump (MD5 Hash: ef2453bff7ad0c4bfa9ab0bd6324ebf3), then select the generated  .apbombh patch file to produce a .z64 ROM which should auto launch in a bizhawk instance. You should be set otherwise from here just follow the same instructions as any other supported N64 apworld.

## Issues
If you encounter any issues with the apworld Please submit them [here](https://docs.google.com/forms/d/1uTGP-_iSZFyEcMNvduUPeF-K2RvlDntGcjgo6BfxgJs)
## Features
- Stages shuffled as checks to collect; get a specified number of clear points in your stage to receive a second check!
- Each Adok Bomb is also a check!
- Fire Ups and Bomb Ups shuffled as only four each in your checks, but are now permanent even after death
- Playable currently up to Bagular
- Collect all 24 Adok Bombs and defeat Bagular to win!
- Deathlink implemented
- Play with random music, sound effects, and skyboxes!

## Gameplay Notes
- Though this game IS easy to pick up and begin, please note that setting your check requirement to 5 Clear Points in your YAML requires that you 100% the stage.
- The Bomb Up and Fire Up items within levels have no effect and will probably be replaced later.
- Certain Boss Room stages unlock early in logic but don't expect you to get your Clear Point check until you get more power ups. You can always go back later and try again!
- If you select an Area with no levels unlocked, you'll be sent back to Planet Bomber Area 1 to prevent crashing.
- Currently (and perhaps indefinitely) the level Emerald Tube does not have a Clear Point check. It feels nearly impossible with Bizhawk's performance issues and I can't find a way around it. Please don't report this as a bug.

## Known Issues
- Random Skybox is still kinda janky and can cause crashes, use at your own risk
- Certain enemies in some stages disappear under certain circumstances. This, as far as we know, is an emulator bug, so please don't report it. Thank you!
- The Clear Point logic is still in its fledgling stages and kind of tuned high right now. If something seems a bit unreasonable to clear at the expected power level, let us know!
- Typos, typos, typos. Please report typos. We will never be annoyed by reporting even the most minor typos!!

## Planned Features
- Secret Gossick Star implementation
