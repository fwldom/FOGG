import turtle
num = int(turtle.textinput(title="Enter Number Forward", prompt=("Enter Forward !")))
numr1 = int(turtle.textinput(title="Enter Number Range", prompt=("Enter Number Range Main !")))
numr2 = int(turtle.textinput(title="Enter Number Range", prompt=("Enter Number on Range Main !")))
num2 = int(turtle.textinput(title="Enter Number left", prompt=("Enter left Range !")))
num3 = int(turtle.textinput(title="Enter Number Right", prompt=("Enter left End Range  !  ")))
width = int(turtle.textinput(title="Enter Number width", prompt=("Enter width !  ")))
laki = turtle.Turtle()
laki.shape('turtle')
laki.width(width)
for i in range(numr1):
    for j in range(numr2):
        laki.forward(num)
        laki.left(num2)
    laki.right(num3)
input()