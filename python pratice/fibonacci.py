a = 0
b = 1
c = 0
print (c)
print (b)
count = 10

for i in range(count-2):
    c = a + b
    
    a = b
    b = c
    
    print(c)  
