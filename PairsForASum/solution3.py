data = [1,2,3,4,5]
sum = 10

covered_values = set()
def findPairs(data):
    for index_outer, value_outer in enumerate(data):
        rem_val = sum - value_outer
        
        if rem_val in covered_values:
            print("Pairs : ", value_outer, rem_val)

        covered_values.add(value_outer)        


findPairs(data)

# Big o = O(n)
from bigO import BigO
lib = BigO()
complexity = lib.test(findPairs, "random",True, True)

