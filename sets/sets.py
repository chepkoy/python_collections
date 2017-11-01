set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

# union
set3 = set1.union(set2)
print(set3)
print(set1 | set2)

# Difference

difference = set1.difference(set2)
print(difference)


difference_two = set2.difference(set1)
print(difference_two)
print(set2-set1)

# uniqeness
print(set1 ^ set2)
print(set2.symmetric_difference(set1))

# Intersection
print(set1.intersection(set2))
print(set1 & set2)