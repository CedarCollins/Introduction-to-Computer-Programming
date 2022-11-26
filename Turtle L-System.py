"""
Sample Inputs:

Enter iterations: 4
Enter length: 10
Enter angle: 60
Enter axiom: >>>>FXF--FF--FF
Enter new rule 'LHS -> RHS' (empty line to exit): X -> --FXF++FXF++FXF--
Enter new rule 'LHS -> RHS' (empty line to exit): F -> FF

Enter iterations: 3
Enter length: 16
Enter angle: 60
Enter axiom: >>>>>>>FX
Enter new rule 'LHS -> RHS' (empty line to exit): X -> X+YF++YF-FX--FXFX-YF+
Enter new rule 'LHS -> RHS' (empty line to exit): Y -> -FX+YFYF++YF+FX--FX-Y

Enter iterations: 6
Enter length: 3
Enter angle: 11.25
Enter axiom: --------X
Enter new rule 'LHS -> RHS' (empty line to exit): X -> F[---X]F[++X]-X
Enter new rule 'LHS -> RHS' (empty line to exit): F -> >>FF<<
"""
import turtle

def createLSystem(iterations,axiom,rules):
    start_string = axiom
    end_string = ""
    for i in range(iterations):
        end_string = processString(start_string,rules)
        start_string = end_string
    return end_string

def processString(oldstring,rules):
    newstring = ""
    for ch in oldstring:
        newstring = newstring + applyRules(ch,rules)
    return newstring

def applyRules(ch,rules):
    newstring = ""
    for rule in range(len(rules)):
        if ch == rules[rule].split(' -> ')[0]:
            newstring = rules[rule].split(' -> ')[1]
            break
        else:
            newstring = ch
    return newstring

def drawLsystem(t,instructions,angle,length):
    saved_info = []
    pen_width = 1
    for cmd in instructions:
        if cmd == 'F':
            t.forward(length)
        elif cmd == 'B':
            t.backward(length)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        elif cmd == '[':
            saved_info.append([t.heading(),t.xcor(),t.ycor()])
        elif cmd == ']':
            new_info = saved_info.pop()
            t.penup()
            t.setheading(new_info[0])
            t.setposition(new_info[1],new_info[2])
            t.pendown()
        elif cmd == '>':
            pen_width = pen_width + 1
            t.width(pen_width)
        elif cmd == '<':
            pen_width = pen_width - 1
            t.width(pen_width)
        else:
            pass

def main():
    print("""Symbols: 'F'=MoveForward, 
         'B'=MoveBackward, 
         '+'=TurnRight, 
         '-'=TurnLeft, 
         '>'=PenWider, 
         '<'=PenNarrower, 
         '['=StateSave, 
         ']'=StateRestore,
         'ACDEGHIJKLMNOPQRSTUVWXYZ'=TurtleIgnores
          """)
    
    iterations = int(input("Enter iterations: "))
    length = float(input("Enter length: "))
    angle = float(input("Enter angle: "))
    axiom = input("Enter axiom: ")

    rules_list = []
    moreRules = True    
    while moreRules:
        new_rule = [input("Enter new rule 'LHS -> RHS' (empty line to exit): ")]
        if new_rule == ['']:
            moreRules = False
        else:
            rules_list = rules_list + new_rule 

    instructions = createLSystem(iterations,axiom,rules_list)
    print(instructions)

    tim = turtle.Turtle()
    tim.hideturtle()
    tim.speed(0)
    wdw = turtle.Screen()
    wdw.tracer(False)
    drawLsystem(tim,instructions,angle,length)
    wdw.tracer(True)
    wdw.exitonclick()

if __name__ == "__main__":
    main()
