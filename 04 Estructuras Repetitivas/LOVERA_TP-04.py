nums = [1,2,3,4,5]

result = 1 
for num in nums:
    result *= num
    if result > 10:
        break
print(result)