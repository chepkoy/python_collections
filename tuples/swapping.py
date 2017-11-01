# Swapping values of variables
# Unpacking
a = 5
b = 20

a, b = b, a

print(a)
print(b)

# Packing into a  tuple

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return  total

print(add(5,5))

# using args

def addition(base, *args):
    total = base
    for num in args:
        total += num
    return total

print(add(5, 20))



