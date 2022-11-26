"""
Sample Inputs:

Enter int angle: 59
Enter int range: 100

Enter int angle: 60
Enter int range: 200
"""
str_angle=input("Enter int angle: ")
int_angle=int(str_angle)

str_range=input("Enter int range: ")
int_range=int(str_range)

a=1
b=1
c=1

import turtle
window=turtle.Screen()
tim=turtle.Turtle()
window.colormode(1)

for i in range(int_range):
    tim.pencolor(a,b,c)
    a=(a-(1/int_range))
    b=(b-(1/int_range))
    c=(c-(1/int_range))
    tim.forward(i)
    tim.left(int_angle)

window.exitonclick()
