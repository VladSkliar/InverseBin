import math
# bin = [1, 0, 1, 1, 0, 1]


def check_remain(x, bin_list):
    if (x % (-2)) == 0:
        bin_list.insert(0, 0)
    elif (x % (-2)) != 0:
        bin_list.insert(0, 1)
    return bin_list


def bin_inverse(bin_list):
    z = len(bin_list)
    x = 0
    for i in range(0, z):
        x += bin_list[i] * ((-2)**(z - i - 1))
    inverse_x = -x
    new_bin_list = []
    while inverse_x != 0:
        inverse_x = float(inverse_x)
        if inverse_x > 0:
            new_bin_list = check_remain(inverse_x, new_bin_list)
        else:
            new_bin_list = check_remain(inverse_x, new_bin_list)
        inverse_x = math.ceil(inverse_x / (-2))
    return new_bin_list

# print bin_inverse(bin)
