# EXERCISE 1

# def sum_to(num):
#   sum = 0
#   for n in range(1, num + 1):
#     sum += n
#   return sum
# print(sum_to(6))


#EXERCISE 2

# def largest(nums):
#   largest = 0
#   for num in nums:
#     if num > largest:
#       largest = num
#   return largest
# print(largest([10, 15, 96, 85, 3]))


#EXERCISE 3

def occurances(str1, str2):
  return str1.count(str2)
print(occurances('fleep floop', 'p'))