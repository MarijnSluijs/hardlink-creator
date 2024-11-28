import os
import tkinter
from tkinter import filedialog
import tkfilebrowser

def mk_hardlink(original_file, hardlink):
    print("original_file: ", original_file)
    # If original file is folder, create hardlink for all files in the folder
    if os.path.isdir(original_file):
        # Make the hardlink folder
        os.makedirs(hardlink, exist_ok=True)
        # Iterate over all files in the folder
        for file in os.listdir(original_file):
            mk_hardlink(f"{original_file}\\{file}", f"{hardlink}\\{file}")
    else:
        # Create the hardlink
        print("hardlink: ", hardlink)
        print(f'mklink /D /H "{hardlink}" --original file: "{original_file}"')
        os.system(f'mklink /D /H "{hardlink}" "{original_file}"')

tkinter.Tk().withdraw()

# Open a window that asks the user whether they want to create a hardlink for a file or a folder
directory = False
while True:
    choice = input("Do you want to create a hardlink for  file(s) or folder(s)? (file/folder) ").lower()
    if choice == "file":
        break
    elif choice == "folder":
        directory = True
        break
    else:
        print("Invalid input. Please try again.")

if directory:

    root = tkinter.Tk()
    root.geometry('200x200')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    original_folders = []

    def get_directories():
        # Ask for the location of the folder containing the original files
        original_folders.append(tkfilebrowser.askopendirnames())
        print("original_folder: ", original_folders)

        # Create the hardlink(s)
        location_of_hardlinks = filedialog.askdirectory(title="Select the folder where the hardlinks will be created").replace("/", "\\")
        print("location_of_hardlinks: ", location_of_hardlinks)

        # Loop over all folders
        for folder in original_folders[0]:
            mk_hardlink(folder, f"{location_of_hardlinks}\\{os.path.basename(folder)}")

    b1 = tkinter.Button(root, text='select directories...', command=get_directories)
    b1.pack()
    print("Done!")

    root.mainloop()

else:
    # Ask for the location of the original file
    location_of_original_files = filedialog.askopenfilenames(title="Select the original file(s)")
    location_of_original_files = [file.replace("/", "\\") for file in location_of_original_files]

    # Create the hardlink(s)
    location_of_hardlinks = filedialog.askdirectory(title="Select the folder where the hardlinks will be created").replace("/", "\\")

    for file in location_of_original_files:
        # Get the filename (the name until folder_name)
        filename = os.path.basename(file)
        file = file.replace("/", "\\")
        print(f"mklink /H '{location_of_hardlinks}\\{filename}' '{file}'")
        # Create the hardlink
        os.system(f'mklink /D /H "{location_of_hardlinks}\\{filename}" "{file}"')


print("Done!")
input("Press Enter to exit...")