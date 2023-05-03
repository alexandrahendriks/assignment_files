__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

'''You need to master the following to complete this assignment:

    Importing and using Python modules;
    Reading and understanding Python standard library documentation.'''

#modules
import os
import zipfile
from zipfile import ZipFile

cwd = os.getcwd()

#Defining path
cache ="cache"
file = "files"
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

#clean_cache()

# Unpacking zip file into cache folder
def cache_zip(file_path, cache_dir_path):
    with ZipFile(file_path, "r") as zip_object:
        zip_object.extractall(cache_dir_path)
        return  

#cache_zip((f"{file_path}/data.zip"), cache_dir_path)

def cached_files():
    cache_files = []
    cache_path = cache_dir_path
    files = os.listdir(cache_path)
    for file in files:
        cache_files.append(f"{cache_path}\{file}")
    return cache_files

#cached_files()


#Finding the password
def find_password(list):
    word = "password"
    for file in list:
       with open(file, "r") as f:
        content = f.read()
        if word in content:
           begin = content.find("correct")
           password = content[begin:136]
           break
    return password

#find_password(cached_files())    