import turtle
num = int(turtle.textinput(title="Enter Number", prompt=("Enter forward !")))
num2 = int(turtle.textinput(title="Enter Number", prompt=("Enter left to shekl !")))
num3 = int(turtle.textinput(title="Enter Number", prompt=("Enter left har bar !  ")))
width = int(turtle.textinput(title="Enter Number", prompt=("Enter width !  ")))
laki = turtle.Turtle()
laki.shape('turtle')
laki.width(width)
for i in range(50):
    for j in range(8):
        laki.forward(num)
        laki.left(num2)
    laki.left(num3)
input()