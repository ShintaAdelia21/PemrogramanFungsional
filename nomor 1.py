def sum_squares(n) :
    sum = 0
    for i in n:
        sum = i ** 2 + sum
    print('hasilnya =', sum)

sum_squares([1, 2, 3])