import os

for a in os.listdir(path='./'):
 #   print(type(a))
    
    with open("newfile.txt","r") as p:
        for line in p:
  #          print(type(line))
            f=line.strip()
            if f in a:
                print(a)
                os.rename(a,f)
 #           else:
 #               print("not found")
           
