#______OK+_______

#prompt for items
#stop when user ctrl-d
#if stop, output full grocery list in uppercase, sorted alphabetically by item
#every item must have the number of inputs
#case insensitive


def main():
    mylist = {

    }

    while True:
        try:

            #get item all in uppercase, no blank spaces
            item = input("Item: ").strip().upper()
            

            #mylist.get(item,0) returns 0 if item not in list, otherwise returns its value
            mylist[item] = mylist.get(item, 0) + 1
            
        except EOFError:

            #loop on my dictionary, put in alphabetical order
            for d in sorted(mylist):
                print(f"{mylist[d]} {d}")
            #print full list
            break


if __name__ == "__main__":
    main()