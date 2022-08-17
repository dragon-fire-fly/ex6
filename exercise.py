#### Exercise 6 ####

##########################
#### ---- Task 1 ---- ####
##########################

# Original buggy code:

# three_mul = 'fizz
# # five_mul = 'buzz'
# # num1 = 3
# # num2 = 4 
# # max_num = 100
   
# # for i in range(1,max_number):
# #     # % or modulo division gives you the remainder
    
# #     if i%num1 = 0:
# #         print(i, three_mul)
# #     elif i%num2 == 0:
# #         print(i, five_mul)
# #     elif i%num1 == 0 and i%num2 == 0:

# #     print(i, three_mul+five_mul)


# #     # 1. 'fizz' only has one '
# #     # 2. num2 should be 5
# #     # 3. in for loop, max_number should be max_num
# #     # 4. in the first if statement, = should be ==
# #     # 5. in the second elif, print should be indented
# #     # 6 & 7. the second elif should be the if and the others should be elifs so that it checks for 'fizzbuzz' before the others

# # Rewritten code:

three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5 
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0:
        print(i, three_mul+five_mul)
    elif i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)
    else:
        print(i)
    
##########################
#### ---- Task 2 ---- ####
##########################

# # Original code: 
# n = 5
# number = 1
# sum = 0
# while number < n + 1:
#     sum = sum + 1
#     number = number + 1
# print("Sum =", sum)

# Fixed code:
n = 5
number = 1
sum = 0
while number < n + 1:
    sum = sum + number
    number = number + 1
print("Sum =", sum)


# # # Bug: during the while loop, sum should be sum + number, not sum +1
# # # This means that it adds the next integer next round

##########################
#### ---- Task 3 ---- ####
##########################

# Original code:
# n = 5
# sum = 0
# for num in range(n):
#     sum += num
# print("Sum =", sum)

# # Fixed code
n = 5
sum = 0
for num in range(n+1):
    sum += num
print("Sum =", sum)

# # Bug: range needs to be n+1, not just n

##########################
#### ---- Task 4 ---- ####
##########################

# #---- Part 1 ----#

for x in range(3):
    print(x)

# # # Bug: needs a colon after the range function

# #---- Part 2 ----#

for j in range(5):
    print(f"This is loop number {j}")

# # or: 

# for j in range(5):
#     print("This is loop number", j)

# # # Bug: it is just printing the letter j. Needs an f-string or comma.

# #---- Part 3 ----#

x = 10

while x > 0:
    print(x)
    x -= 1
    
# # Bug: x is defined after the while loop, but it must be before as the value is required for the loop

# #---- Part 4 ----#

countdown = 5
while countdown >=1:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")

# # Bug: countdown needs a value and the while loop needs a condition to evaluate 
# #(before it was evaluating whether 'countdown' was True or False)

##########################
#### ---- Task 5 ---- ####
##########################

# # Original code:
# x = input("First number: ")
# y = input("Second number: ")
# z = input("Third number: "))

# if x = y or y = z:
#     result = 0
# else:
#     sum = x + y + z
# print("Calculated sum is ", result)

# # Bugs: 1. An extra bracket at the end of z input line
# #       2. if statement should be evaluating with ==, not =
# #       3. if statement should also be evaluating if x and z are equal
# #       4. calculated sum should be "sum", not "result"
# #       5. values should be converted to integers to prevent string concatenation

# #rewritten code:
x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or x == z:
    result = 0
else:
    result = x + y + z
print("Calculated sum is ", result)


##########################
#### ---- Task 6 ---- ####
##########################

# # Original code
# x = input("First number: ")
# y = input("Second number: ")

# result = x + y

# if result > 15 or result < 20:
#     sum = 20
# print("Calculated sum is ", ressult)

# # Bugs: 1. ressult is spelled wrong. Should be 'result'
# #       2. inputs should be converted to integer values
# #       3. if statment should be >= and <= to include 15 and 20 in the value range
# #       4. 'sum' variable should be 'result' so it can be printed
# #       5. if statement should be 'and', not 'or' (otherwise will return 20 for all sums less than 20, 
# # #         rather than just 15-20)

# # Fixed code
x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    result = 20
print("Calculated sum is ", result)

# # alternative:
# if 15 <= result <= 20:
#     result = 20

##########################
#### ---- Task 7 ---- ####
##########################

a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " ,b = ", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, " ,b = ", b)

# Bugs: 1. need to use input to request input from user
#       2. syntax needed updating in both print statements to it prints the value of the b variable 
#           and not just the string 'b'
#       3. b needs to be assigned the value of 'temp' which was the original value of a
#       4. the input should not be converted to an integer using the int() function as the user then 
#           cannot enter other data types such as strings

##########################
#### ---- Task 8 ---- ####
##########################

# # Original code:
# x == input("First number: ")
# y == input("Second number: ")
# z == input("Third number: ")

# print("The maximum value is ", (x, y ,z))
# print("The minimum value is ", abs(x, y ,z))

# Fixed code
# x = float(input("First number: "))
# y = float(input("Second number: "))
# z = float(input("Third number: "))

# print("The maximum value is ", max(x, y ,z))
# print("The minimum value is ", min(x, y ,z))

# Bugs: 1. the inputs should be assigned with "=", not "=="
#       2. the max value should be calculated using the max() function
#       3. the min value should be calculated using the min() function, not the abs() function

x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))


##########################
#### ---- Task 9 ---- ####
##########################

x = input("Type your value: ")

if x == "0":
    x = False
elif x == "1":
    x = True

print("Your entered value is now", x)

# Alternative, but cannot enter strings:
# x = int(input("Type your value: "))

# if x == 0:
#     x = False
# elif x == 1:
#     x = True

# print("Your entered value is now", x)

# Bugs: 1. missing " at end of input
#       2. for if and elif statements, x should be evaluated using "==", not "="
#       3. True and False should be capitilised
#       3. else statement is redundant (if used, pass should be indented)
#       4. must check x against "0" and "1" (instead of 0 and 1) as x is automatically a str and conversion to int would mean that strings 
#         (such as "hi" can't be entered

###########################
#### ---- Task 10 ---- ####
###########################
# Original code:
# x = input("First number: ")
# y = input("Second number: ")

# if x %% y >= 0:
#     print("First number is divisible by second number, result =", x // y)
# elif y %% y != 0:
#     print("Second number is divisible by first number, result =", y // x)
# else:
#     print("Numbers are non-divisable!")

# Bugs: 1. inputs must be converted to integer values using int() 
#       2. functiononly ned one % sign (not %%)
#       3. comparitor should be == 0, not >=0 or !=0
#       4. elif statement should be y%x, not y%y 
#       5. only need 1 x / not //
#       5. spelling error

# Corrected code:
x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", x / y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y / x)
else:
    print("Numbers are non-divisible!")