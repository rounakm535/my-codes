# num = int(input("Enter the num"))
# count = 0
#
# for i in range(1, num):
#     if num % i == 0:
#         count += 1
# print(count)
# if count == 1:
#     print("The number is prime")
#
# else:
#     print("The number is not prime")

# 1-100 3 - fin, 5- buzz, 3,5raunak

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0 :
#         print("Rounak")
#
#     elif i % 5 == 0 :
#         print("Buzz")
#
#     elif i % 3 == 0 :
#         print("Fizz")
#
#     else:
#         print(i)


# second highest no in list of size 10

lis = [99, 88, 70, 101, 50, 60, 121, 80, 90, 100]

maximum = lis[-1]
sec_max = lis[-1]

for num in lis:
    if num > maximum:
        sec_max = maximum
        maximum = num
    elif num > sec_max and num != maximum:
        sec_max = num


print(sec_max)
