#breakfast: 7:00 - 8.00
#lunch: 12:00 - 13:00
#dinner: 18:00 - 19:00

def format_check(time):
    #check presence of :
    if ":" not in time:
        print("Error in time format: format must be #:## or ##:##")
        return None
    
    hm = time.split(":") #hours minutes
    
    #check presence of both parts 
    if len(hm) != 2:
        print("Error in time format (error2)")
        return None
    
    hh , mm = hm

    if not (hh.isdigit() and mm.isdigit()):
        print("Format error: some parts of the input are not digits")
        return None
    
    #return a tuple
    return hh, mm


def convert(time):

    format_ch = format_check(time)

    #check the format
    if format_ch is None:
        return None
    
    
    #unpack the tuple
    str_h , str_m = format_ch #returns a tuple

    #convert in floats, with max 2 decimals
    ih = int(str_h)
    im = int(str_m)
    

    #check for value errors in the minutes
    #max time: 23:59 (in 24h format you don't have 24:00)
    if not (0<= ih <= 23 and 0<= im <= 59):
            print("Value error")
            return None
    return ih+(im*0.01)
        

def main():
    #ask time to user in format #:## or ##:## (24h)
    wtime = input("What's the time? ") #-> what time
    
    #remove white spaces
    wtime = wtime.strip() 

    ctime = convert(wtime)

    if ctime is None:
        return

    if (7.00 <= ctime <= 8.00):
        print(f"It's {ctime:.2f} so it is breakfast time!")
    elif (12.00 <= ctime <= 13.00):
        print(f"It's {ctime:.2f} so it is lunch time!")
    elif (18.00 <= ctime <= 19.00):
        print(f"It's {ctime:.2f} so it is dinner time!")
    else:
        print(f"I'm sorry you're hungry but it's not meal time")


if __name__ == "__main__":
    main()
