import math

def circle(rad):
    for y in range(-rad,rad+1):
        my_string = " "
        for x in range(-rad,rad+1):
            if math.sqrt((x**2)+(y**2)) > rad:
                my_string += ("  ")
            else:
                my_string += ("* ")
        print(my_string)
        
def main():
    moreCircles = True
    while moreCircles:
        integer = int(input("Enter positive integer radius (0 to quit): "))
        if integer != 0:
            circle(integer)
        else:
            moreCircles=False
    print("Quiting program now...")
    
if __name__ == "__main__":
    main()
