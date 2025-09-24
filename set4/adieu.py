#______OK_______
#prompt user for names until the user inputs control-d
#assumption: the usel will input at least one name

#function used to create the list of names
def nameslist():
    names =[]
    while True:
        #base = "Adieu, adieu, to "
        try:
            name = input("New name: ")
            if name:
                #names.append(name)
                names.append(name)
        except EOFError:
            print()
            return names
            #when the user inputs ctrl-d i have to return the list of names



#takes the names list and formats it correctly 
def formatNames(listofnames):
    base = "Adieu, adieu, to "

    #if len(list) == 0: 
    #    return ""
    
    #base case: only 1 element
    if len(listofnames) == 1:
        return base + listofnames[0]
    
    elif len(listofnames) == 2:
        return base + f"{listofnames[0]} and {listofnames[1]}"
    
    else:
        #base = "adieu (..) to" 
        # + 1st element in the list of names 
        # + ', ' -> add a comma after all the elements of the list, but the last one
        #, and
        #{listofnames[-1]} -> last element
        return base + f"{', '.join(listofnames[:-1])}, and {listofnames[-1]}"
        #format(list[1:]) = call on slice of list without the first element
        #but taken from element 2

def main():
    names = nameslist()
    formatted = formatNames(names)
    print(formatted)


if __name__ == "__main__":
    main()

