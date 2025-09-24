#count LOC to measure program complexity

#
#open file
#count lines
#return lines number

import sys #-> work with argv
def main():
    #verify cmd input
    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif len(sys.argv) == 2:
        name = sys.argv[1]
        if not name.endswith(".py"):
            sys.exit("Not a python program")

        #open the program
        try:
            with open(name, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            sys.exit("File not found")

        #count the lines
        count = 0
        for line in lines:
            no_w_spaces = line.lstrip()
            if no_w_spaces == "":
                continue
            if no_w_spaces.startswith("#"): #comments
                continue
            count +=1

        print(count)

if __name__ == "__main__":
    main()

