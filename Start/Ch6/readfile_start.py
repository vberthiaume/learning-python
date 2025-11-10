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