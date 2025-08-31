#SUMBISSION:
#mkdir um
#files: um.py, test_um.py
#check50 cs50/problems/2022/python/um
import re
import sys 
def main():
    print(count(input("Text: ")))

#in: str; out: n: int, n= repetitions of 'um'
def count(s):

    #\b = word boundary -> finds um even if close to ounctuation
    pattern = (r"\bum\b")
    num = len(re.findall(pattern, s , flags = re.IGNORECASE))
    return num

if __name__ == "__main__":
    main()