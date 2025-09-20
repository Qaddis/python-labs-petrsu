fib_nums = [0, 1]

for i in range(2, 1001):
    res = fib_nums[0] + fib_nums[1]

    fib_nums[0] = fib_nums[1]
    fib_nums[1] = res

print(fib_nums[1])
