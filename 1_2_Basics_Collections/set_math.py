set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 9, 11, 13, 17, 19, 23}

my_union = set1.union(set2)
#Could also call union method using the following operator;
my_union = set1 | set2

my_difference1 = set1.difference(set2)
# or the following operator
my_difference1 = set1 - set2

my_difference2 = set2.difference(set1)
#or the following operator
my_difference2 = set2 - set1

my_symmetricdifference = set1.symmetric_difference(set2)
#or the following operator
my_symmetricdifference = set1 ^ set2

my_intersection = set1.intersection(set2)
#or the following operator
my_intersection = set1 & set2

# issubset uses <= and < as operators
if set1 <= set2:
    subset_test1 = True
else:
    subset_test1 = False

# issuperset uses >= and > as operators
if set1 >= set2:
    superset_test1 = True
else:
    superset_test1 = False

print('Set 1 is {}'.format(set1))
print('Set 2 is {}'.format(set2))
print('The union of the 2 sets is {}'.format(my_union))
print('The difference between set1 and set2 is {}'.format(my_difference1))
print('The difference between set2 and set1 is {}'.format(my_difference2))
print('The symmetric difference between the two sets are {}'.format(my_symmetricdifference))
print('The intersection of the two sets are {}'.format(my_intersection))
print('set1 is a subset of set2: {}'.format(subset_test1))
print('set1 is a superset of set2: {}'.format(superset_test1))