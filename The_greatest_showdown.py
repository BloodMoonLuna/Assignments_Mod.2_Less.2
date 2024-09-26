#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.
#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.
#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))


if num1 >= num2 and num3:
    print(str(num1) + " is the largest.")
elif num2 >= num1 and num3:
    print(str(num2) + " is the largest.")
elif num3 >= num1 and num2:
    print(str(num3) + " is the largest.")

if num1 <= num2 and num3:
    print(str(num1) + " is the smallest.")
if num2 <= num1 and num3:
    print(str(num2) + " is the smallest.")
if num3 <= num1 and num2:
    print(str(num3) + " is the smallest.")