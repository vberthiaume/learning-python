# ============================ Create a file and write to it ============================

# the list of possible arguments for w+ here is the same as in the fopen c function: https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
sample_file = open("text.txt", "w+")
sample_file.write("brooooooo")
sample_file.close()

# Now re-open that file and append to it
sample_file = open("text.txt", "a+")
sample_file.write("braaaa")
sample_file.close()

# ============================ now read that file ============================

# Open the file and read the contents
sample_file = open("text.txt", "r")

# use the read() function to read the entire file
if sample_file.mode == "r":
    contents = sample_file.read()
    print(contents)

# if we don't close the file first, we can't read into it again
sample_file.close()
sample_file = open("text.txt", "r")

# use the read() function to read the entire file
if sample_file.mode == "r":
    file_lines = sample_file.readlines()
    for line in file_lines:
        print(line)

# ============================ now a bit more advanced file manipulations ============================
# to open and write to files we don't need to import stuff, but for more advanced stuff we do
import os
from os import path
import time
import datetime
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("item exists: ", path.exists("text.txt"))
print("item is a file: ", path.isfile("text.txt"))
print("item is a directory: ", path.isdir("text.txt"))

# Work with file paths
print("item's path", path.realpath("text.txt"))
print("item's path and name", path.split(path.realpath("text.txt")))

# Get the modification time
mtime = path.getmtime("text.txt")
modifiedclocktime = time.ctime(mtime)
print(modifiedclocktime)

# Calculate how long ago the item was modified
modifiedtimestamp = datetime.fromtimestamp(mtime)
td = datetime.now() - modifiedtimestamp
print(f"it has been {td} since the file was modified")
print(f"or, {td.total_seconds()} seconds")

# ================================== now some zip file faffing =============================

import shutil
from zipfile import ZipFile

filename = "text.txt"
if path.exists(filename):
    # make a duplicate of an existing file
    src = path.realpath(filename)
    dst = src + ".bak"
    shutil.copy(src,dst)

    # rename the original file -- not doing it because it'll mess up everything else lol
    # os.rename(filename, "newFile.txt")

# now put things into a ZIP archive
rootdir, tail = path.split(src)
shutil.make_archive("archive", "zip", rootdir)

# more fine-grained control over ZIP files
# this with business is a context manager
# which will close the file automatically when we're done
with ZipFile("testzip.zip", "w") as newzip:
    newzip.write(filename)
    newzip.write(dst)   #dst is available even though it was created in a local scope above

# ======================== final test ========================================

# test: count the size of bytes of text files in the "deps" directory
def file_info():
    size = 0
    cur = os.getcwd() # "deps" 
    if path.isdir(cur):
        for f in os.listdir(cur):
            fullpath = path.join(cur, f)
            if path.isfile(fullpath) and fullpath.endswith(".txt"):
                size += path.getsize (fullpath)

    return size

print (file_info())