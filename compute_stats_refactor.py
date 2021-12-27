from math import sqrt

file = "random_nums.txt"


def read_ints():
    data = []
    with open(file, "r") as f:
        for line in f:
            num = int(line)
            data.append(num)
    return data


def count():
    i = 0
    for n in read_ints():
        i += 1
    return i


def summation():
    data = read_ints()
    nums_sum = 0
    for num in data:
        nums_sum += num
    return nums_sum


def average():
    return summation() / count()


def maximum():
    data = read_ints()
    max_num = None
    for num in data:
        if max_num is None or num > max_num:
            max_num = num
    return max_num


def minimum():
    data = read_ints()
    min_num = None
    for num in data:
        if min_num is None or num < min_num:
            min_num = num
    return min_num


def harmonic_mean():
    data = read_ints()
    sum_of_inverses = 0
    for num in data:
        if num == 0:
            # The harmonic mean can not be computed when zero values are present
            # See https://rdrr.io/cran/lmomco/man/harmonic.mean.html
            return None
        sum_of_inverses += 1 / num
    return count() / sum_of_inverses


def is_a_sample():
    min_population_size = 30
    return count() < min_population_size


def variance():
    data = read_ints()
    avg = average()
    sqr_diff_with_mean = 0
    for x in data:
        sqr_diff_with_mean += (x - avg)**2
    n = count()
    if is_a_sample():
        if n > 1:
            n -= 1
    return sqr_diff_with_mean / n


def standard_dev():
    return sqrt(variance())


if __name__ == '__main__':
    print("read_ints:", read_ints())
    print("count:", count())
    print("summation:", summation())
    print("average:", average())
    print("maximum:", maximum())
    print("minimum:", minimum())
    print("harmonic_mean:", harmonic_mean())
    print("variance:", variance())
    print("standard_dev:", standard_dev())
