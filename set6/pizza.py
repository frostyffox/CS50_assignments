import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too many or too few arguments")

    fname = sys.argv[1]

    if not fname.endswith(".csv"):
        sys.exit("not a csv file")

    #open the csv
    try:
        with open(fname, newline="") as ff:
            read = csv.reader(ff)
            data = list(read)
    except FileNotFoundError:
        sys.exit("File not found")

    #the file is empty
    if not data:
        sys.exit("this file is empty")

    head = data[0]
    row = data[1:]

    print(tabulate(row, headers=head, tablefmt="grid"))

if __name__ == "__main__":
    main()
