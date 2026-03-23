import os

folders = input("Enter a list of folder paths separated by spaces: ").split()

for folder in folders:
    files = os.listdir(folder)
    print("========listing files for the folder - " + folder)
    
    for file in files:
        print(file)