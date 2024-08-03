with open("my_file.txt") as file:
    content = file.read()
    print(content)


with open("mfile.dat", mode ="w" ) as file:
    age = input("What is your current age")
    file.write(age)
