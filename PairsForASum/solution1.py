data = [1,2,3,4,5]
sum = 9

def findPairs(data):
    for index_outer, value_outer in enumerate(data):
        print("index outer: ", index_outer)
        for index_inner, value_inner in enumerate(data[index_outer+1:]):
            print(index_outer, index_inner)
            if (value_outer  + value_inner) == sum:
                print("The pairs are : ",",".join([str(value_outer), str(value_inner)]))

# Big o = O(n^2)
from bigO import BigO
lib = BigO()
complexity = lib.test(findPairs, "random",True, True)
