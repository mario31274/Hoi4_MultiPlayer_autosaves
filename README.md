# Hoi4_MultiPlayer_autosaves

This is a very basic script I created to backup multiplayer autosaves. It copys the autosave into a specified backup directory ever *copy_delay* seconds if the new autosave is more than *delta_minutes_min* minutes older than the most recent backup file. When the backup directory has more than *max_saves*, it deletes the oldest file in the backup directory.

Hearts of Iron doesnt let you use folders for saves, so **to load a backup auto save you need to copy it back into the save directory.**

### Caution

This script might not work for you. It was created on windows and has not been tested on any other systems.

**Runing programs on the internet can be dangerous.**

### Caveats and other warnings

- There is very little error checking in the script. 
- If you over ride the backup directory to "", it will the oldest save if there are more than *max_saves* in the "save games" folder
- The autosave file name is hard coded to "autosave.hoi4", if you want to backup any other file name this requires a change in the code.

## How to run Script

***This script is writen in python and requires python 3 to run.***

The script can be called in via your python instaliation as:

    python */pathtoscript*/backup_hoi4_saves.py

If you want to run with any non default values for the parameters, you can instead run with any number of parameters

    python */pathtoscript*/backup_hoi4_saves.py max_saves=52 delta_minutes_min=5 copy_delay=60 backup_dir=r"backup_mp/" maxtime=86400

### Troubleshooting tips

If you have having issues running the script. Try just running python

    python
    
This should result in launching python in the console and will state the version info and give a prompt that looks like:

    >>>

For some cases you will have to specify the path for python. For example I have my python installed via anaconda so I have to run the script as follows:

    C:\Users\UserNameHere\anaconda3\python.exe */pathtoscript*/backup_hoi4_saves.py

And if I just run

    python
    
It brings up the windows store to install python.


##  backup_hoi4_saves.py
    
    Change the auto save setting in the game to specify the frequency of the autosaves.

    This will copy any save that is $delta_minutes_min$ older than the last backup.

    Only $max_saves$ are kept in $backup_dir$/, after that the oldest saves are deleted.

    :param max_saves: Max Files to keep in backup_dir
    :param delta_minutes_min: Minimum minutes between backup saves
    :param copy_delay: Minimum minutes between backup saves
    :param backup_dir: Folder within save dir to backup saves
    :type backup_dir:str
    :param maxtime: Stop the script after __ seconds
    
    
