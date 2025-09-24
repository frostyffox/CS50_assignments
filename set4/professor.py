import random

def main():
    level = get_level()
    score = 10
    for i in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y 
        attempt = 0
        while attempt < 3:
            try:
                res = int(input(f"{x} + {y} = "))
                if res == z:
                    score +=1
                    break
                else:
                    print("EEE")
                    attempt +=1
            except ValueError:
                print("EEE")
                attempt +=1
        if attempt == 3:
            print(f"{x} + {y} = {z}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            #level
            l = int(input("Level: "))
            levs = [1,2,3]
            if l in levs:
                return l
        except ValueError:
            print("Enter a valid int. Level: ")

    

def generate_integer(level):
    #random number of level digits
    #if level = 1 -> 1<=n<10 | 1^10
    #if level = 2 -> 10<=n<100
    #if level = 3 -> 100<=n<1000
    n = random.randint(10**(level-1), 10** level-1)

    #10**(1-1) = 10**0=1; 10**1 -1 = 10-1 =9
    #...
    return n

if __name__ == "__main__":
    main()