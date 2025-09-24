#1 row = 3 values
#goal: reformat name

import sys
import csv

def main():
    #check arguments
    if len(sys.argv) != 3:
        sys.exit("Too few or too many arguments")

    finput = sys.argv[1]
    fout = sys.argv[2]

    #read the data in csv 1
    try:
        with open(finput, newline="") as fin:
            read = csv.DictReader(fin) #data is a dict
            students = list(read)
    except FileNotFoundError:
        sys.exit("File not found")

    for student in students:
        last, first = student['name'].split(", ")
        student['first'] = first.strip()
        student['last'] = last.strip()

    #create csv output
    col_names = ['first','last','house']
    with open(fout, "w", newline="") as fo :
        write = csv.DictWriter(fo, fieldnames= col_names)
        write.writeheader()
        for student in students:
            write.writerow({
                'first': student['first'],
                'last': student['last'],
                'house': student['house']
            })
if __name__ == "__main__":
    main()
