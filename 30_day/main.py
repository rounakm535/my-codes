# try:
#     file = open("a_file.txt", "r")
#     arr = [1, 2, 3, 4]
#     print(arr[3])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "a")
#     file.write("Something")
#
# except IndexError:
#     print("Give the right index value")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("File closed")


# bmi calc

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be more than 3 meters")

bmi = weight / height ** 2

print(bmi)