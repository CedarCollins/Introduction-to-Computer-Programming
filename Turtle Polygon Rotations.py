"""
Sample inputs:

Enter rotational copies: 5
Enter sides per polygon: 4
Enter edge pixel length: 200

Enter rotational copies: 5
Enter sides per polygon: 5
Enter edge pixel length: 200

Enter rotational copies: 8
Enter sides per polygon: 6
Enter edge pixel length: 150

Enter rotational copies: 12
Enter sides per polygon: 8
Enter edge pixel length: 120

Enter rotational copies: 8
Enter sides per polygon: 3
Enter edge pixel length: 300
"""
import turtle
import random

#function coloring the background
def randbg():
    a=random.choice([0.0,0.25])
    b=random.choice([0.0,0.25])
    c=random.choice([0.0,0.25])
    return (a,b,c)

#function creating the polygon
def polygon(t,s,l):
    for x in range(s):
        t.forward(l)
        t.left(360/s)

#function rotating and copying polygon 
def shape(t,r,s,l):
    for x in range(r):
        polygon(t,s,l)
        t.left(360/r)

def main():
    #inputs and printed info
    randbg1=randbg()
    print("Random background color is:",randbg1)
    rotations=int(input("Enter rotational copies: "))
    sides=int(input("Enter sides per polygon: "))
    length=int(input("Enter edge pixel length: "))
    print("Click turtle screen to exit...")

    #sets up turtle
    wn=turtle.Screen()
    wn.bgcolor(randbg1)
    tim=turtle.Turtle()
    tim.hideturtle()

    #draws larger white lines
    tim.color("white")
    tim.pensize(5)
    shape(tim,rotations,sides,length)

    #draws inner colored lines
    tim.color("black")
    tim.pensize(1)
    shape(tim,rotations,sides,length)
    
    wn.exitonclick()

if __name__ == "__main__":
    main()
