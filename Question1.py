# Naive Approach: Using a simple loop
def naive_sum(int_list):
    total = 0
    for num in int_list:
        total += num
    return total

# Recursive Approach
def recursive_sum(int_list):
    if not int_list:
        return 0
    return int_list[0] + recursive_sum(int_list[1:])

# Using Built-in Functions
def builtin_sum(int_list):
    return sum(int_list)


int_list = [1, 2, 3, 4, 5]
print("Naive Approach Sum:", naive_sum(int_list))
print("Recursive Approach Sum:", recursive_sum(int_list))
print("Built-in Function Sum:", builtin_sum(int_list))
