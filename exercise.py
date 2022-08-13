#### Exercise 6 ####
#---- Task 1 ----#

# three_mul = 'fizz
# five_mul = 'buzz'
# num1 = 3
# num2 = 4 
# max_num = 100
   
# for i in range(1,max_number):
#     # % or modulo division gives you the remainder 
    
#     if i%num1 = 0:
#         print(i, three_mul)
#     elif i%num2 == 0:
#         print(i, five_mul)
#     elif i%num1 == 0 and i%num2 == 0:
#     print(i, three_mul+five_mul)


#     # 1. 'fizz' only has one '
#     # 2. num2 should be 5
#     # 3. in for loop, max_number should be max_num
#     # 4. in the first if statement, = should be ==
#     # 5. in the second elif, print should be indented
#     # 6. the second elif should be the if and the others should be elifs so that it checks for 'fizzbuzz' before the others

# three_mul = 'fizz'
# five_mul = 'buzz'
# num1 = 3
# num2 = 5 
# max_num = 100
   
# for i in range(1,max_num):
#     # % or modulo division gives you the remainder 
    
#     if i%num1 == 0 and i%num2 == 0:
#         print(i, three_mul+five_mul)
#     elif i%num1 == 0:
#         print(i, three_mul)
#     elif i%num2 == 0:
#         print(i, five_mul)
    
#---- Task 2 ----#

# n = 5
# number = 1
# sum = 0
# while number < n + 1:
#     sum = sum + number
#     number = number + 1
# print("Sum =", sum)


# # Bug: during the while loop, sum should be sum + number, not sum +1
# # This means that it adds the next integer next round

#---- Task 3 ---- #

# n = 5
# sum = 0
# for num in range(n+1):
#     sum += num
# print("Sum =", sum)

# Bug: range needs to be n+1, not just n

#---- Task 4 ----#

# for x in range(3):
#     print(x)

# # Bug: needs a colon after the range function


#---- Task 5 ----#
#---- 1 ----#

# for j in range(5):
#     print(f"This is loop number {j}")

# # Bug: it is just printing the letter j. Needs an f-string or comma.

#---- 2 ----#

# x = 10

# while x > 0:
#     print(x)
#     x -= 1
    
# Bug: x is defined after the while loop, but it must be before as the value is required for the loop

#---- 3 ----#

# countdown = 5
# while countdown >=1:
#     print(f"{countdown}")
#     countdown -= 1
# else:
#     print("Start!")

# Bug: countdown needs a value and the while loop needs a condition to evaluate (before it was evaluating whether 'countdown' was True or False)

#---- 4 ----#

# x = input("First number: ")
# y = input("Second number: ")
# z = input("Third number: "))

# if x = y or y = z:
#     result = 0
# else:
#     sum = x + y + z
# print("Calculated sum is ", result)

# Bugs: 1. An extra bracket at the end of z input line
#       2. if statement should be evaluating with ==, not =
#       3. if statement should also be evaluating if x and z are equal
#       4. calculated sum should be "sum", not "result"
#       5. values should be converted to integers to prevent string concatenation

#rewritten code:
# x = int(input("First number: "))
# y = int(input("Second number: "))
# z = int(input("Third number: "))

# if x == y or y == z or x == z:
#     result = 0
# else:
#     sum = x + y + z
# print("Calculated sum is ", sum)


#---- Task 6 ----#

x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    result = 20
print("Calculated sum is ", result)

# Bugs: 1. ressult is spelled wrong. Should be 'result'
#       2. inputs should be converted to integer values
#       3. if statment should be >= and <= to include 15 and 20 in the value range
#       4. 'sum' variable should be 'result' so it can be printed
#       5. if statement should be 'and', not 'or' (otherwise will return 20 for all sums less than 20, rather than just 15-20)

