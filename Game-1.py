import turtle
from random import randint

from classes import Point, GuiPoint, GuiRectangle

rectangle_1 = GuiRectangle(Point((randint(0, 440)), (randint(0, 400))),
                           Point((randint(1, 400)), (randint(1, 400))))

print(f"Rectangle's points = ({rectangle_1.point_1.x, rectangle_1.point_1.y}) ,"
      f" ({rectangle_1.point_2.x, rectangle_1.point_2.y})")
point = GuiPoint(int(input("Guess the x number.")), int(input("Guess the y number")))


if point.falls_in_rectangle(rectangle_1):
    print("Yes, point is in the rectangle.")
else:
    print("No, point is not in the rectangle.")

user_area = int(input("Guess the area of rectangle."))
print(f"The deviation is = {rectangle_1.calculate_area() - user_area}")

myturtle = turtle.Turtle()
rectangle_1.draw(canvas=myturtle)
point.draw(canvas=myturtle)
turtle.done()
