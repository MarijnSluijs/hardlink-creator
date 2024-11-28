# Hardlink Creator
This script creates hardlinks of files chosen by the user in Windows.

This script has 2 steps: 
1. The script first asks the user to choose all the files of which a hardlink should be created.
2. The script asks the user to choose the location of the hardlinks. 

When multiple files are chosen in step 1, all hardlinks will be placed at the location chosen in step 2.

## How to use
Run "python hardlink_creator.py" in the terminal.

OR 

Click on the .bat file

## Dependencies
Python has to be installed, along with the following imports:
- tkinter (pip install tk)
- tkfilebrowser (pip install tkfilebrowser)

These might also be needed:
- pywin32 (pip install pywin32)
- pypiwin32 (pip install pypiwin32)