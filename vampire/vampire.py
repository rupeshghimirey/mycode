#!/usr/bin/env python3
# read the file and close it and readlines read all the lines from the textfile
count = 0
# writing file in a single file
out_file = open("vampytimes.txt", "w")

# reading file 
with open('dracula.txt','r') as vampireBlog:
    all_lines = vampireBlog.readlines()

    for line in all_lines:
        if "vampire" in line.lower():
            print(f"{count+1}) {line}", end = "", file = out_file)
            count += 1;
print(f"Vampire count is: {count}")

