#_______outdated.py________

#US format: mmddyyyy = middle endian
#computer format: yyyymmdd = iso 8601
    #y: 4 digits
    #m,d : 2 digits (ex: 06, 17, 01)

#prompt user for a date in american format (mmddyyyy)
#month can be a number or name
#if invalid format: prompt again

#output date in format yyyy-mm-dd
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def indate():
    while True: #continues until ctrl-d
        spacers = [" ",",","/","-"]
        try:
            #ask for date
            idate = input("Date in format mmddyyyy: ").strip()
                #the elements of the date can be separated by " ", ",", "-", or "/"
            for spa in spacers:
                idate = idate.replace(spa, " ")
                #now i can split with spaces
            if len(idate.split()) != 3:
                continue
            mm, dd, yyyy = idate.split()
            #first part is not a word:
            if mm.isdigit():
                mm = int(mm)
            else: #firt part is a word
                mm = mm.title()

                #the word is in the month dictionary
                if mm in months: #if the month is written with characters
                    mm = months.index(mm) + 1
                    #mm is still an integer now
                #not in months dictionary
                else:
                    continue
            dd = int(dd)
            yyyy = int(yyyy)
            #checking that months, days and years have valid values
            if not(0<mm<13 and 0<dd<=31 and yyyy>=0):
                continue
            return mm, dd, yyyy


        except EOFError: #user has pressed control-d
                #new line
            print("\n")
            break

def main():
    mm, dd, yyyy = indate()

    #month needs a 0
    if mm<10:
        smm =f"0{mm}"
    else:
        smm = f"{mm}"
    if dd<10: 
        sdd = f"0{dd}"
    else:
        sdd = f"{dd}"

    print(f"Date re-formatted: {yyyy}-"+smm+"-"+sdd)

if __name__ == "__main__":
    main()


