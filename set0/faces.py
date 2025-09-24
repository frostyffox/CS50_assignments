#convert
#takes a string; returns the string converting :) and ): to the corresponding emojis
def convert(input_str):
    converted = input_str.replace(":)","🙂" ).replace(":(","🙁").replace("):","🙁")
    return converted

#main
def main():
    text = input("Write here your message ")
    print(convert(text))

main()