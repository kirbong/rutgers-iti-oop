# Assignment 3

test_list = [3, 7, 1]
n = 5

def sum_int_list(arg_list):
    return sum(test_list)


# Hint: use the power operator ** 
# see https://docs.python.org/3/reference/expressions.html#the-power-operator
def power_int_list(arg_list, n):
    result_power = [pow(n, 2) for n in test_list]
    return result_power

def power_sum_int_list(arg_list, n):
    result_power = [pow(n, 2) for n in test_list]
    result_sum = sum(result_power)
    return result_sum


print('Result of sum_int_list: {}'.format(sum_int_list(test_list)))
print('Result of power_int_list: {}'.format(power_int_list(test_list, n)))
print('Result of power_sum_int_list: {}'.format(power_sum_int_list(test_list, n)))