data = [1,2,3,4,5]
sum = 10

def findPairs(data):
    for index_outer, value_outer in enumerate(data):
        rem_values = set(data[index_outer+1:])
        rem_val = sum - value_outer

        if rem_val in rem_values:
            print("Pairs : ", value_outer, rem_val)


findPairs(data)




# Big o = O(n^2)
# from bigO import BigO
# lib = BigO()
# complexity = lib.test(findPairs, "random",True, True)

