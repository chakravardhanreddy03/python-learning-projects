def average(numbers):
    total = 0
    for i in range(len(numbers) + 1):
        total += numbers[i]
    return total / len(numbers)

nums = [10, 20, 30, 40]

print("Average:", average(nums))

if average(nums) > 25:
    print("Above 25")
else:
    print("25 or below")