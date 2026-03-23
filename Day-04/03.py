import sq_module
import sys
def add(num1,num2):
    add = num1 + num2
    return add

def diff(num1,num2):
    diff = num1 - num2
    return diff

def mul(num1,num2):
    mul = num1 * num2
    return mul

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

plus = add(num1,num2)


num2sq = sq_module.square(num2)
print(num2sq)
print(plus)
print(sq_module.pi)