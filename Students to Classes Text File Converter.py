"""
Please keep a text file (students.txt) in the same directory location as the python file in the following format:

    <Student>: <Class 1> <Class 2> ... <Class n>
"""

def dictionary(classes):
    d = {}
    infile = open("students.txt","r")

    for item in classes:
        d[item] = []
    
    for line in infile:
        name = line.split(": ")[0]
        for item in classes:
            if item in line:
                d[item] = d[item] + [name]
    infile.close()
    return d
    
def write(classes):
    print('Writing output file "classes.txt"...')

    try:
        outfile = open("classes.txt","w")

    except IOError:
        print("Error: classes.txt can't be opened for output.")

    else:
        d = dictionary(classes)
        for key in d:
            value = d.get(key)
            outfile.write(key + ":\n")
            for item in value:
                line = str(item) + "\n"
                outfile.write(line)
            outfile.write("\n")
        outfile.close()
        print("Output processed.")

def main():
    print('Reading input file "students.txt"...')
    
    try:
        infile = open("students.txt","r")

    except IOError as e:
        print("Error: students.txt does not exist or it can't be opened for input.")

    else:
        student_list = []
        all_classes_list = []
        
        for line in infile:
            split = line.split(": ")
            space_split = ((split[1][:-1]).split())
            all_classes_list = all_classes_list + space_split

        classes_list = []
        [classes_list.append(x) for x in all_classes_list if x not in classes_list]
        classes_list = sorted(classes_list)
        print("Input processed.")
        
        write(classes_list)
        
        infile.close()

    finally:
        print("Program exiting now...")
    

if __name__ == "__main__":
    main()
