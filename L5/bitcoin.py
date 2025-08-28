#********OK********
import requests
import sys

#convention: if using sys.exit() 
#-> do all the checks in auxiliary function; use main just for output

def btcToUsd():

    #_______handling input (arg)______
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")


    #_______checking format________
    try:
        #expect the user to specify as a cmd arg, n = number of bitcoins they want to buy
        #conversion to float
        n = float(sys.argv[1])
    #if n cannot be converted in float:
    except ValueError:

        #exit via sys.exit and error message
        sys.exit("Command-line argument is not a number")

    #________fetch current bictoin value_____
    #query the API for the CC bitc price index
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c3ca5f4158bf7dbd441b5d0effc7dd4eb741071b5f49baf868521952530b2eff")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("API request failed")   

    #______deal with JSON____________ 
    value = response.json()
    cvalue = float(value["data"]["priceUsd"])

    return cvalue*n

def main():
    result = btcToUsd()
    #check if the function returns a value
    #format: #,###.####
    print(f"${result:,.4f}")
    
if __name__ == "__main__":
    main()