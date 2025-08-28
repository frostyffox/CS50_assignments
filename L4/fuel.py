#___________OK_________
#return a % int 
#if <= 1% : output E
#if >= 99% : output F
#prompt user again if 
    #x or y not int
    #x>y -> 
    #y=0 -> ZeroDivisionError
def inFraction():
    while True:
        try:

            #prompt for a fraction in format x/y where x,y > 0, int
            fraction = input("Fraction in format X/Y: ")

            #check if / is present
            if "/" not in fraction:
                raise ValueError("Fraction must contain "/"")
            
            #split in x,y (still strings)
            xs , ys = fraction.split("/")

            #check if both are digits
            if not (xs.isdigit() and ys.isdigit()):
                raise ValueError("x and y must be integers")
            
            #convert to integers
            x ,y = int(xs), int(ys)

            #check if denomin ==0
            if y==0:
                raise ZeroDivisionError("Denominator cannot be zero")
            
            if x<=0 or y <=0:
                raise ValueError("Both X and Y must be > 0.")
            
            if x > y :
                raise ValueError("X must be < Y")
            
            return x,y
        
        except ValueError:
            print(ValueError)
        except ZeroDivisionError:
            print(ZeroDivisionError)

def main():
    x , y = inFraction()
    percent = round((x/y)*100)

    if percent >= 99 :
        print('F')
    elif percent <= 1:
        print('E')
    else:
        print(f"Fuel Status: {percent}%")

if __name__ == "__main__":
    main()


