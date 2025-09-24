import string

#get input from user

def is_valid(strg):
    #check lenght
    l = len(strg)
    if not 2<= l <= 6:
        return False
    
    #all alphanumeric 
    if not strg.isalnum():
        return False
    
    #str[0] and str[1] must be letters
    if not strg[0:2].isalpha():
        return False

    #check for punctuation marks
    if any(char in string.punctuation for char in strg):
        return False 

    #loop to look for numbers
    # if the first digit found is zero, invalid

    #enumerate returns (index, character)
    for idx, ch in enumerate(strg):
        if ch.isdigit():
            if  ch == "0":
                return False
            #after i find a digit, the rest must be number
            if not strg[idx:].isdigit():
                return False
            break
    return True

    


def main():

    while True:
        try:
            plate = input("Plate: . press ctrl-d to exit\n")
            if is_valid(plate):
                print("Valid")
            else:
                print("Invalid")
        except EOFError:
            print("\nBYE\n")
            break

        

if __name__ == "__main__":
    main()