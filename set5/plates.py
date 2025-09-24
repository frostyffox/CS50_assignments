#_______OK_______

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


#req:
#1 first to character mucht be letters -> ok
#2 len is <= 2 and >=6 -> ok
#3 the first number used cannot be a zero
#4 no periods, spaces or punctuation marks -> 4
# numbers only in the middle of the plate

def is_valid(s):

    s = s.strip()

    #2
    if not (2 <= len(s) <= 6):
        return False

    #4
    if not s.isalnum() :
        return False

    #1
    if not s[0:2].isalpha():
        return False

    #3
    snum = ""
    for n,c in enumerate(s) :
        if c.isdigit():
            if c == '0': #stops the first time it finds a digit if it is 0
                return False

            #i found a digit but is not 0
            #i need the rest of the plate to be digits
            if not s[n:].isdigit(): #n:] chesch all the characters of s from position n onwards
                return False
            break


    return True

if __name__ == "__main__":
    main()
