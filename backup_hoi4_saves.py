import os,sys
from os import listdir
from os.path import isfile, join
import shutil
import datetime
from datetime import date
from datetime import timedelta
from pathlib import Path
import time

def backup_hoi4_saves(max_saves=52,delta_minutes_min=5,Copy_delay=60,backup_dir=r"backup_mp/",maxtime=86400):
    """
    Change the auto save setting in the game to specify the frequency of the autosaves.

    This will copy any save that is $delta_minutes_min$ older than the last backup.

    Only $max_saves$ are kept in $backup_dir$/, after that the oldest saves are deleted.

    :param max_saves: Max Files to keep in backup_dir
    :param delta_minutes_min: Minimum minutes between backup saves
    :param Copy_delay: Minimum minutes between backup saves
    :param backup_dir: Folder within save dir to backup saves
    :type backup_dir:str
    :param maxtime: Stop the script after __ seconds
    """

    ts = time.time()
    savegame_dir=os.path.abspath(os.path.expanduser("~/Documents/Paradox Interactive/Hearts of Iron IV/save games/"))

    print("Save Game folder: {}".format(savegame_dir))
    backup_path = os.path.join(savegame_dir, backup_dir)
    try:
        os.mkdir(backup_path)
        print("Created backup folder : {}".format(backup_path))
    except:
        print("Backup folder : {}".format(backup_path))
        pass
    autosave=os.path.join(savegame_dir,"autosave.hoi4")

    if not os.path.isfile(autosave):
        sys.stderr.write("Autosave not found at : {}".format(autosave))
        exit()

    while time.time() < ts + maxtime:
        filetimes=[]
        for file in os.listdir(backup_path):
            filetimes.append(datetime.datetime.fromtimestamp(os.stat(backup_path+file).st_mtime))

        autosave_time = datetime.datetime.fromtimestamp(os.stat(autosave).st_mtime)

        if autosave_time > max(filetimes)+datetime.timedelta(minutes=delta_minutes_min):
            shutil.copyfile(autosave, backup_path + "autosave" + autosave_time.strftime("%m.%d.%H.%M") + ".hoi4")

        while len(filetimes) > max_saves:
            files=[Path(backup_path + file) for file in os.listdir(backup_path)]
            files.sort(key=os.path.getmtime)
            oldest_file=files[0]
            print("Removing {}".format(oldest_file))
            os.remove(oldest_file)
        time.sleep(copy_delay)


# Run with over ride defaults
backup_hoi4_saves(max_saves=52,delta_minutes_min=5,Copy_delay=60,backup_dir=r"backup_mp/",maxtime=86400)
