
count = {}
with open("./source.txt", "r") as f:
    for line in f:
        if "500" in line:
            count["500"] = count["500"] + 1
    
print (count)