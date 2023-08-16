__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#modules
import os
from zipfile import ZipFile

cwd = os.getcwd()

#Defining path
cache ="cache"
data = "data.zip"
cache_dir_path = os.path.join(cwd, cache)
file_path = os.path.join(cwd, data)

# Creating cache folder if it doesn't exist and if it does deleteing all files from it
def clean_cache():
    if os.path.exists(cache_dir_path):
        print("Folder found")
        files = os.listdir(cache_dir_path)
        for file in files:
            os.remove(os.path.join(cache_dir_path, file))
    elif not os.path.exists(cache_dir_path):
        os.chdir(cwd)
        os.mkdir(cache)
    return

# Unpacking zip file into cache folder
def cache_zip():
    with ZipFile(file_path, "r") as zip_object:
        zip_object.extractall(cache_dir_path)
        return  

def cached_files():
    cache_files = []
    cache_path = cache_dir_path
    files = os.listdir(cache_path)
    for file in files:
        cache_files.append(os.path.join(cache_path, file))
    return cache_files

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

if __name__  == "__main__":
    clean_cache()
    cache_zip()
    cached_files()
    find_password(cached_files())  