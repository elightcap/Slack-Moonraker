# Slack-Moonraker

## Commands
- /getprinter: no args, just returns some info about the printer. oa few other commands call this function also
- /setextemp: args(int target_temperature), sets the extruder to the requested temperature
- /setbedtemp: args(int target_bed_temperature), sets the bed to the requested temperature
- /preheat: args(string filament_type), preheats bed and extruder to defined temperatures
- /sethome: no args, just sends printer a g28 to home all axes
- /slice: args(string file_name, string profile_name), slices the named file using the requested profile

## shortcuts
- upload: this one is weird, need to make a shortcut, upload a file, then use the shortcut to upload the file to the print server. it can then be sliced with `/slice`, and ill probably get  `/print` command in someday