# Hoi4_MultiPlayer_autosaves

This is a very basic script I created to backup multiplayer autosaves.

It was created on windows and may or may not work on other operating systems. It requires python to run.

The script can be called in via your python instaliation as:

    python /pathtoscript/backup_hoi4_saves.py

If you want to run with any non default values for the parameters, you can instead run with any number of parameters

    python /pathtoscript/backup_hoi4_saves.py max_saves=52 delta_minutes_min=5 copy_delay=60 backup_dir=r"backup_mp/" maxtime=86400


backup_hoi4_saves.py

    Change the auto save setting in the game to specify the frequency of the autosaves.

    This will copy any save that is $delta_minutes_min$ older than the last backup.

    Only $max_saves$ are kept in $backup_dir$/, after that the oldest saves are deleted.

    :param max_saves: Max Files to keep in backup_dir
    :param delta_minutes_min: Minimum minutes between backup saves
    :param copy_delay: Minimum minutes between backup saves
    :param backup_dir: Folder within save dir to backup saves
    :type backup_dir:str
    :param maxtime: Stop the script after __ seconds
    
    
