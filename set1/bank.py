
def greet_fee(fee, greeting):
    if ('hello' in greeting):
        return fee
    elif (greeting.startswith('h')):
        fee += 20
        
    else:
        fee += 100
       
    return fee


def main():

    #set the default fee value
    fee = 0

    #ask to formulate the greeting
    greeting = (input("Greet the customer ")).lstrip().lower()

    #evaluate the greeting fee
    greet_fee(fee, greeting)

    print("the bank owes the customer", fee, "$")

main()