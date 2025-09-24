
def remover(in_put):

    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    novow = ""
    for c in in_put:
        if c not in vowels:
            novow += c

    return novow

def main():
    in_put = input("Input: ")
    if in_put :
        cleaned = remover(in_put)

        print("Output: "+ cleaned)

if __name__ == "__main__":
    main()