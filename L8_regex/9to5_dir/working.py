import re
import sys


def main():
    print(convert(input("Hours: ")))

#format
#i will find for sure: number, AM, to, number, PM
#optional: :00, :00
#return: n:00 to m:00
#input: "n(:mm) AM to m(:mm) PM"
    # (:mm) optionals> ?: = 'make a unique 2nd group';
    #\s space

#output: "HH:MM to HH:MM"
def convert(s):
    #extract
        #group1,4: hours. > \d{1,2}
        #g2,5: optional minutes; ?: = 'make a unique 2nd group';(:\d{2})) ("optional element with : and 2 digits")
        #\s* space (zero or many); \s? (zero or 1 space)
        #g3,6: am/pm 
    pattern = (r"^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$")
    #validate
    match = re.search(pattern,s, re.IGNORECASE)
    if not match: 
        raise ValueError
    
    #HOURS
    h1 = int(match.group(1))
    h2 = int(match.group(4))

    if not ( 1 <=h1 <= 12) or not  (1 <= h2 <= 12):
        raise ValueError("invalid hour")
        terminate
    
    
    #MINUTES

    m1 = match.group(2)
    if m1 is not None:
        m1 = int(m1)
    else: 
        m1 = 0
    
    m2 = match.group(5)
    if m2 is not None:
        m2 = int(m2)
    else:
        m2 = 0
    
    if not (0<= m1 <= 59) or not (0<= m2 <= 59):
        raise ValueError("invalid minute format")
    
    #AM/PM
    period1 =match.group(3)
    period2 =match.group(6)
    
    #convert in 24h
   
    if period1 == "AM":
        if h1 == 12:
            h1 = 0
    elif period1 == "PM":
        if h1 != 12:
            h1 += 12
    if period2 == "AM":
        if h2 == 12:
            h2 = 0
    elif period2 == "PM":
        if h2 != 12:
            h2 += 12
    #format and return; 
    return (f"{h1:02}:{m1:02} to {h2:02}:{m2:02}")




if __name__ == "__main__":
    main()
