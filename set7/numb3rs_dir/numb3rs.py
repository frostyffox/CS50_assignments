#numb3rs


#IP address: 275.3.6.28
#IPv4: num identifier formatted as #.#.#.#
# 0<= # <=255
import re
import sys

#ip = str
#out: True/False

#numbers from 0 to 99: [1-9]?[0-9]. [1-9]? -> optional leading digit
#from 100 to 199: 1[0-9]{2} : 1, 2x(something between 0 and 9)
#from 200 to 249: 2[0-4][0-9]
#249-255: 25

def validate(ip):
    pattern = (r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}"
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$")

    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False

def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()
    