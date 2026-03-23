import os

folders = input("Enter a list of folder paths separated by spaces: ").split()

for folder in folders:
    
    try:
        
        files = os.listdir(folder)
    
    except FileNotFoundError:
        print("please provide valid folder name, " + folder + " doesn't exist")
        break
    
    print("========listing files for the folder - " + folder)
    
    for file in files:
        print(file)