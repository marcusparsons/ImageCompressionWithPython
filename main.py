from PIL import Image
import PIL
from pathlib import Path
import glob
import tkinter
from tkinter import filedialog

# Pillow library required to run image compression
# python -m pip install --upgrade Pillow

def get_filename(path):
    return Path(path).name

root = tkinter.Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames(parent=root, title='Choose a file')

if file_paths != '':
    filelist = root.tk.splitlist(file_paths)

    for file_path in filelist:
        file_name = get_filename(file_path)
        picture = Image.open(file_path)

        picture.save("Compressed_%s" % file_name, optimize=True, quality=50) 
        print('Compressed picture saved for %s' % file_name)
