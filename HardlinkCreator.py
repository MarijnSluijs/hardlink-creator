import os
import tkinter
from tkinter import filedialog
# os.system(r"mklink /H C:\Users\marij\OneDrive\Documents\Projects\HardlinkCreator\Test\tmp.txt C:\Users\marij\OneDrive\Documents\Projects\HardlinkCreator\tmp.txt")

tkinter.Tk().withdraw()

# Ask for the original file(s)
location_of_original_files = filedialog.askopenfilenames(title="Select the file(s) you want to create a hardlink of")

# Ask for the location of the hardlink(s)
location_of_hardlinks = filedialog.askdirectory(title="Select the folder where you want to create the hardlink(s)").replace("/", "\\")

for file in location_of_original_files:
    # Get the filename
    filename = os.path.basename(file)
    file = file.replace("/", "\\")
    print(f"mklink /H '{location_of_hardlinks}\\{filename}' '{file}'")
    # Create the hardlink
    os.system(f'mklink /H "{location_of_hardlinks}\\{filename}" "{file}"')

print("Done!")
input("Press Enter to exit...")