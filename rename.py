import os

with open("filename.txt","r") as f:
    for line in f:
        print (line[2:9])
        with open("newfile.txt","a") as p:
            p.write(line[2:9])
            p.write("\n")