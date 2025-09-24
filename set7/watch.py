#for cs50 submission: file name = watch.py
#
#
# #embed link -> html lines
#iframe: html element
#src: html attribute with value "https://www.youtube.com/embed/xvFZjo5PgG0"

#example of minimal html: <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# extract the urls from the html codes
# sub youtube > youtu.be
#rm /embed

#from 'src="https://www.youtube.com/embed/#######"'
#to "https://youtu.be/######""

import re
import sys

def main():
    print(parse(input("HTML: ")))

#input: 'src=(...)'
#out: https://youtu.be(...)
def parse(s):

    if not s:
        return None
    #eliminate ...src=
    # ^ = start of string; .*? match all the characters eventually before src
    # then find the actual src
    # in https? letter s is optional
    # www\.youtube\.com -> use the \ because otherwise . has a different meaning
    # don't include /embed in the substitution
    #out: "https://ww.youtube.com/embed/########"

    pattern = r'<iframe[^>]*\s+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    match = re.search(pattern,s)

    if match:
        id = match.group(1)
        return f"https://youtu.be/{id}"
    else:
        return None

    #final = re.sub(r'^.*?src="https?://(www\.)?youtube\.com/embed/', 'https://youtu.be/', s )
    #return final

if __name__ == "__main__":
    main()


