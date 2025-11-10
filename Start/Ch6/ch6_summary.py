import os
from os import path

# test: count the size of bytes of text files in the "deps" directory
def file_info():
    size = 0
    cur = "deps" # os.getcwd()
    if path.isdir(cur):
        for f in os.listdir(cur):
            if f.endswith(".txt"):
                size += path.getsize (path.join(cur, f))

    return size

file_info()