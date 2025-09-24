#______OK______
import random

def level():
    while True:
        try:#prompt user for a level n
            n = int(input("Level: "))
            if n > 0:
                break
            else:
        #if input != integer, positive -> re-prompt
                print("Level (>0): ")
        except ValueError:
            print("Level (valid int): ")
    l = random.randint(1,n)
    return l

def guessing(l):
#randomly generate l
    #l=int, 1=<l<=n (inclusive)
    while True:
        try:
            g = int(input("Guess: "))
            if g <= 0: 
                print("Must be > 0")
                continue

            if g == l :
                print("Just right!")
                break
            elif g < l:
                print("Too small!")
                #continue -> not necessary
            elif g>l:
                print("Too big!")
                #continue -> not necessary
        except ValueError:
            print("Input a valid integer")

#prompt user to guess l
    #if guess (g) < l -> print("Too small") -> prompt again
    #if g > l -> printI("Too large") -> prompt again
    #if g == l -> print("Just right") -> exit
def main():
    l = level()
    guessing(l)

if __name__ == "__main__":
    main()