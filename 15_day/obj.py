from turtle import Turtle , Screen

kalu = Turtle()
print(kalu)
kalu.shape("turtle")
kalu.color("blue")
kalu.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmaeder"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# print(table)