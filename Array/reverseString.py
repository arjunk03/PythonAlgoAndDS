# Solution 1
#
def reverse_string(value):
    return "".join(value[::-1])


output = reverse_string("My name is arjun")
print(output)


# Solution 2
#
def reverse_string2(value):
    return "".join(list(reversed(value)))


output = reverse_string2("My name is arjun")
print(output)


# solution 3
#
def reverse_string3(value):
    strng_val = ""
    for chr in value:
        strng_val = chr + strng_val
    return strng_val


output = reverse_string3("My name is arjun")
print(output)


# solution 4
#
def reverse_string4(value):
    if len(value) == 0:
        return value

    else:
        return reverse_string4(value[1:]) + value[0]


output = reverse_string4("My name is arjun")
print(output)


# SOLUTION 5
#
def reverse_string5(value):
    return "".join([value[ind] for ind in range(len(value), -1, -1)])


output = reverse_string4("My name is arjun")
print(output)


print(list(range(10, -1, -1)))


from functools import reduce


# SOLUTION 6
#
def reverse_string6(value):
    return reduce(lambda x, y: y + x, value)


output = reverse_string6("My name is arjun")
print(output)
