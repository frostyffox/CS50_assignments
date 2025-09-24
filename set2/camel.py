def main():
    camel = input("camelCase: ")
    snake = into_snake(camel)
    print("snake_case: " + snake)

def into_snake(camel):
    snake = ""
    for c in camel:
     
        #i find a capital letter
        if c.isupper():

            #turn capital into small
            cl = c.lower()

            #add underscore and small char to new string
            snake += "_" + cl
        else: 
            snake += c
    return snake


main()