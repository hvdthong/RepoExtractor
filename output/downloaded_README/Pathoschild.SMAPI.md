**SMAPI** is an open-source modding API for [Stardew Valley](http://stardewvalley.net/) that lets
you play the game with mods. It's safely installed alongside the game's executable, and doesn't
change any of your game files. It serves eight main purposes:

1. **Load mods into the game.**  
   _SMAPI loads mods when the game is starting up so they can interact with it. (Code mods aren't
   possible without SMAPI to load them.)_

2. **Provide APIs and events for mods.**  
   _SMAPI provides APIs and events which let mods interact with the game in ways they otherwise
   couldn't._

3. **Rewrite mods for crossplatform compatibility.**  
   _SMAPI rewrites mods' compiled code before loading them so they work on Linux/Mac/Windows
   without the mods needing to handle differences between the Linux/Mac and Windows versions of the
   game._

4. **Rewrite mods to update them.**  
   _SMAPI detects when a mod accesses part of the game that changed in a game update which affects
   many mods, and rewrites the mod so it's compatible._

5. **Intercept errors.**  
   _SMAPI intercepts errors that happen in the game, displays the error details in the console
   window, and in most cases automatically recovers the game. This prevents mods from accidentally
   crashing the game, and makes it possible to troubleshoot errors in the game itself that would
   otherwise show a generic 'program has stopped working' type of message._

6. **Provide update checks.**  
   _SMAPI automatically checks for new versions of your installed mods, and notifies you when any
   are available._

7. **Provide compatibility checks.**  
   _SMAPI automatically detects outdated or broken code in mods, and safely disables them before
   they cause problems._

8. **Back up your save files.**  
   _SMAPI automatically creates a daily backup of your saves and keeps ten backups, in case
   something goes wrong. (Via the bundled SaveBackup mod.)_

## Documentation
Have questions? Come [chat on Discord](https://discord.gg/KCJHWhX) with SMAPI developers and other
modders!

### For players
* [Player guide](https://stardewvalleywiki.com/Modding:Player_Guide)

### For modders
* [Modding documentation](https://stardewvalleywiki.com/Modding:Index)
* [Mod build configuration](mod-build-config.md)
* [Release notes](release-notes.md)

### For SMAPI developers
* [Technical docs](technical-docs.md)
