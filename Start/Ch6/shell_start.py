import os
from os import path
import shutil
from zipfile import ZipFile

filename = "text.txt"
if path.exists(filename):
    # make a duplicate of an existing file
    src = path.realpath(filename)
    dst = src + ".bak"
    shutil.copy(src,dst)

    # rename the original file
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
