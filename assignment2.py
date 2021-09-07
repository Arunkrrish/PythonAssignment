# Write a program to find the prime number 

# Enter a number to program and get the output "Prime" or "Not Prime"

num = int(input("Enter a number: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")