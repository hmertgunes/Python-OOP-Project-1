class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point_1.x < self.x < rectangle.point_2.x and \
                rectangle.point_1.y < self.y < rectangle.point_2.y:
            return True
        else:
            return False


class GuiPoint(Point):

    def draw(self, canvas, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def calculate_area(self):
        return (self.point_2.y - self.point_1.y) * (self.point_2.x - self.point_1.x)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point_1.x, self.point_1.y)
        canvas.pendown()

        canvas.forward(self.point_2.x - self.point_1.x)
        canvas.left(90)
        canvas.forward(self.point_2.y - self.point_1.y)
        canvas.left(90)
        canvas.forward(self.point_2.x - self.point_1.x)
        canvas.left(90)
        canvas.forward(self.point_2.y - self.point_1.y)