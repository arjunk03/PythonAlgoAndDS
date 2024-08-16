array1 = [10, 15, 20]
array2 = [12, 14, 18, 19]


# Soltion 1
#
def sorted_array(array1, array2):
    new_array = array1 + array2

    print(" New array :", new_array)
    length = len(new_array)
    start = 0

    sort_array = []
    while start < length:
        min_val = new_array[start]
        print("min val :", min_val)
        for indx, val in enumerate(new_array[start + 1 :]):
            print(" val : ", val)
            if min_val > val:
                print(" enterrr")
                new_array[start + 1 + indx] = min_val
                min_val = val

        sort_array.append(min_val)
        start += 1

    return sort_array


output = sorted_array(array1, array2)
print(output)
