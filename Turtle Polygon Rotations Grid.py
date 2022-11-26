"""
Sample Input:

Enter rotational copies: 5
Enter sides per polygon: 4
Enter edge pixel length: 100
Enter row range start: -200
Enter row range end: 200
Enter row range increment: 400
Enter col range start: -250
Enter col range end: 250
Enter col range increment: 250
"""
import turtle
import random

def draw_polygon(t,spp,epl):
    for j in range(spp):
        t.forward(epl)
        t.left(360/spp)

def draw_rotational_polygons(t,spp,epl,rc):
    for i in range(rc):
        draw_polygon(t,spp,epl)
        t.left(360/rc)

def draw_full_shape(t,spp,epl,rc):
    epl2 = epl
    while epl2 > 1:
        t.pensize(5)
        t.color(1,1,1)
        draw_rotational_polygons(t,spp,epl2,rc)
        epl2 = ((epl2)/2)

    epl2 = epl
    while epl2 > 1:
        t.pensize(1)
        t.color(0,0,0)
        draw_rotational_polygons(t,spp,epl2,rc)
        epl2 = ((epl2)/2)

def draw_grids(t,spp,epl,rc,rrs,rre,rri,crs,cre,cri):
    rows = int((rre - rrs)/rri)+1
    columns = int((cre - crs)/cri)+1
    col=crs
    row=rrs

    for y in range(rows):
        for x in range(columns):
            t.penup()
            t.goto(col,row)
            t.pendown()
            draw_full_shape(t,spp,epl,rc)
            col = col+cri
        col = crs
        row = row+rri

def main():
    background_red = 0
    background_green = 0
    background_blue = 0
    
    while background_red == 0 and background_green == 0 and background_blue == 0:
        background_red = random.choice([0.0,0.125,0.25,0.375,0.5])
        background_green = random.choice([0.0,0.125,0.25,0.375,0.5])
        background_blue = random.choice([0.0,0.125,0.25,0.375,0.5])
        
    print("Random background color is: (", background_red, ",", background_green, ",", background_blue, ")")

    wn = turtle.Screen()
    wn.bgcolor(background_red, background_green, background_blue)

    murtle = turtle.Turtle()
    murtle.hideturtle()
    murtle.speed(0)

    rotational_copies = int(input("Enter rotational copies: "))
    sides_per_polygon = int(input("Enter sides per polygon: "))
    edge_pixel_length = int(input("Enter edge pixel length: "))

    row_range_start = int(input("Enter row range start: "))
    row_range_end = int(input("Enter row range end: "))
    row_range_increment = int(input("Enter row range increment: "))
    col_range_start = int(input("Enter col range start: "))
    col_range_end = int(input("Enter col range end: "))
    col_range_increment = int(input("Enter col range increment: "))

    #row range is bottom/top bound of centers of shapes
    #row increment is vertical space between centers of shapes

    #col range is left/right bound of centers of shapes
    #col increment is horizontal space between centers of shapes

    draw_grids(murtle,sides_per_polygon,edge_pixel_length,rotational_copies,row_range_start,row_range_end,row_range_increment,col_range_start,col_range_end,col_range_increment)

    print("Click turtle screen to exit...")
    wn.exitonclick()

if __name__ == "__main__":
    main()

