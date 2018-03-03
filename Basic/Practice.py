# # Program to Calculate the Average of Numbers in a Given List.
# n = int(input("Enter the number of elements to be inserted: "))
# a = []
# for i in range(0, n):
# 	elem = int(input("Enter element: "))
# 	a.append(elem)
# avg = sum(a) / n
# print("Average of elements in the list", round(avg, 2))


# a = int(input("Enter value of first variable: "))
# b = int(input("Enter value of second variable: "))
# a = a + b   # a = 10 + 12  22
# b = a - b   # b = 22 - 12  10
# a = a - b   # a = 22 - 10  12
# print("a is:", a, " b is:", b)


# n = int(input("Enter a number n: "))
# temp = str(n)
# t1 = temp+temp
# print(t1)
# t2 = temp+temp+temp
# comp = n + int(t1) + int(t2)
# print("The value is:", comp)


# n = int(input("Enter number: "))
# rev = 0
# while n > 0:
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n // 10
#     print(n)
# print("Reverse of the number:", rev)


# n = int(input("Enter number: "))
# if n > 0:
#     print("Number is positive")
# else:
#     print("Number is negative")


# n = 3  # number of Subjects
# sub = []
# for i in range(0,n):
# 	elem = int(input("Enter marks of the subjects: "))
# 	sub.append(elem)
#
# print(sub)
# avg = sum(sub)//n
# print(avg)
#
# if avg >= 90:
# 		print("Grade: A")
# elif avg >= 80 & avg < 90:
# 		print("Grade: B")
# elif avg >= 70 & avg < 80:
# 		print("Grade: C")
# elif avg >= 60 & avg < 70:
# 		print("Grade: D")
# else:
# 		print("Grade: F")


# lower = int(input("Enter lower range limit:"))
# upper = int(input("Enter upper range limit:"))
# n = int(input("Enter the number to be divided by:"))
# for i in range(lower, upper+1):
# 	if i % n == 0:
# 		print(i)


# one = int(input("Enter lower range limit:"))
# two = int(input("Enter upper range limit:"))
#
# quotient = one/two
# reminder = one % two
# # var = f"quotient is {quotient} & reminder is {reminder}"
# var = "quotient is {:5f} & reminder is {:3d}".format(quotient, reminder)
# print(var)


# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))
# d = []
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if i!= j & j!= k & k!= i:
#                 print(d[i],d[j],d[k])


# n = int(input("Enter range:"))
# for i in range(0,n):
# 	if i % 2 != 0:
# 		print(i)


# n = 123456
# tot = 0
# while n > 0:
# 	reg = n % 10
# 	tot = tot + reg
# 	n = n // 10
# print("Sum of digits is : ",tot)


# n = int(input("Enter an integer:"))
# a = []
# for i in range(2, n+1):
#     if n % i == 0:
#         a.append(i)
# a.sort()
# print("Smallest divisor is:", a[0])


# count = 0
# n = int(input("Enter the input:"))
# while n > 0:
# 	n = n // 10
# 	count += 1
# print("Count of digit is :", count)


# temp = 0
# temp1 = 0
# n = int(input("Enter the input:"))
# a = n
# while n > 0:
# 	temp1 = n % 10
# 	temp = temp * 10 + temp1
# 	n = n // 10
# 	print(temp)
# if temp == a:
# 	print("Paliandrome")
# else:
# 	print("Not Paliandrome")


# for i in range(0, 51):
# 	if i % 2 != 0 and i % 3 != 0:
# 		print(i)
#


# Python Program to Read a Number n And Print the Series “1+2+…..+n= “
# n = int(input("Enter a number: "))
# a = []
# for i in range(1, n + 1):
# 	print(i, sep=" ", end=" ")
# 	if i < n:
# 		print("+", sep=" ", end=" ")
# 	a.append(i)
# print("=", sum(a))
# print()


# n = int(input("Enter a number: "))
# n = 6
# for j in range(1, n + 1):
# 	a = []
# 	for i in range(1, j + 1):
# 		print(i, sep=" ", end=" ")
# 		if i < j:
# 			print("+", sep=" ", end=" ")
# 		a.append(i)
# 	print("=", sum(a))
# print()


# n = 5
# for i in range(0, n):
#     for j in range(0, n):
#         if i == j:
#             print(1, sep=" ", end=" ")
#         else:
#             print(0, sep=" ", end=" ")
#     print()


# n = 5
# for i in range (n,0,-1):
#     print((n-i) * ' ' + i * '*')


# n=10
# sieve=set(range(2,n+1))
# print(sieve)
# while sieve:
#     prime=min(sieve)
#     print(prime,end="\t")
#     sieve-=set(range(prime,n+1,prime))
# print()

