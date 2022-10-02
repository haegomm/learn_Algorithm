# numbers = [1, 5, 8, 6, 3]
#
# print(numbers.sort())  # None
# print(numbers)  # [1, 3, 5, 6, 8]
# print(sorted(numbers))  # [1, 3, 5, 6, 8]

# numbers = [1, 9, 6, 5, 2]
#
# new_numbers = sorted(numbers)
#
# print(numbers)
# print(new_numbers)

answer = [1, 1, 5, 9, 6, 8, 8, 8]

new_answer = sorted(list(set(answer)))

print(answer)
print(new_answer)