inp = str(input("Числа: "))

nums = [int(i) for i in inp.split(" ")]

if max(nums) > 0 and min(nums) < 0:
    a = min(nums)
    b = max(nums)
elif min(nums) > 0:
    a = min(nums)
    del nums[nums.index(a)]
    b = min(nums)
else:
    a = max(nums)
    del nums[nums.index(a)]
    b = max(nums)

print(f"{a} * {b} = {a * b}")
