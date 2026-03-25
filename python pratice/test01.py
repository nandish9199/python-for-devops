import json

with open ("/workspaces/python-for-devops/python pratice/.jason.json") as f:
    j=json.load(f)

#j["Statement"][0]["Effect"]="PublicReadGetObject"
#print(j["Statement"][0]["Effect"])
a = j[0]  # converting to list for append to work
#print(a)
j.append(a)
#print(j)
with open ("/workspaces/python-for-devops/python pratice/.jason.json","w") as f:
    json.dump(j,f,indent=4)