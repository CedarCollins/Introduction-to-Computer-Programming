def main():
    str_empty = str(input("Enter (^madlib^): "))
    str_new = ""

    blank_lines = int(input("Enter number of blank lines to hide the madlib: "))
    for x in range(blank_lines + 1):
        print("")

    moreMLs = True
    
    while moreMLs == True:
        str_new = str_new + str_empty[:str_empty.find("(^")]
        component = str_empty[str_empty.find("(^")+2:str_empty.find("^)")]
        word = input("Enter {}: ".format(component))
        str_new = str_new + word
        str_empty = str_empty[str_empty.find("^)")+2:]
        if str_empty.find("(^") > str_empty.find("^)"):
            str_new = str_new + str_empty[:str_empty.find("(^")+2]
            str_empty = str_empty[str_empty.find("(^")+2:]
        if str_empty.find("(^") == -1 or str_empty.find("^)") == -1:
                moreMLs = False        
                              
    if moreMLs == False:
        str_new = str_new + str_empty
        print(str_new)
   
if __name__ == "__main__":
    main()
