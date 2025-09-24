# DEMO:
# Input: Twitter
# Out: Twttr

#aim: remove vowels
def shorten(word):
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    novow = ""
    for c in word:
        if c not in vowels:
            novow += c

    return novow

def main():
    in_put = input("Input: ")
    if in_put :
        cleaned = shorten(in_put)

        print("Output: "+ cleaned)

if __name__ == "__main__":
    main()
