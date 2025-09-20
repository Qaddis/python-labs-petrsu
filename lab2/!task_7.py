from random import randint

counter = 0
nums = {}

while counter < 1000000:
    num = randint(1, 50)

    if not str(num) in nums.keys():
        nums[str(num)] = 1
    else:
        nums[str(num)] += 1

    counter += 1

for k in nums.keys():
    print(f"{k} - {nums[k]}")

# Доп. проверка
print(sum(nums.values()))
