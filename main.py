__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

'''You need to master the following to complete this assignment:

    Importing and using Python modules;
    Reading and understanding Python standard library documentation.'''

#modules
import os
import zipfile

cwd = os.getcwd()

#Defining path
cache ="cache/"
file = "files/"
cache_dir_path = (f"{cwd}\{file}\{cache}")
file_path = (f"{cwd}\{file}")

# Creating cache folder if it doesn't exist and if it does deleteing all files from it
def clean_cache():
    if os.path.exists(cache_dir_path):
        print("Folder found")
        files = os.listdir(cache_dir_path)
        for file in files:
            os.remove(f"{cache_dir_path}\{file}")
    elif not os.path.exists(cache_dir_path):
        os.chdir(file_path)
        os.mkdir(cache)
    return

clean_cache()

# Unpacking zip file into cache folder
def cache_zip(file_path, cache_dir_path):
    
