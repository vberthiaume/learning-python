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

modifiedtimestamp = datetime.fromtimestamp(mtime)

# Calculate how long ago the item was modified
td = datetime.now() - modifiedtimestamp
print(f"it has been {td} since the file was modified")
print(f"or, {td.total_seconds()} seconds")
