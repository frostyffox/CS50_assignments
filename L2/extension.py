#output file_name.extension
# gif, jpg, jpeg, png = image
# txt = plain (text/plain)
# pdf, zip = application

def main():
#prompt user for file name and saves it getting rid of whitespaces
    f_name = input("File name with extension : ").strip().lower()
    

    if '.' not in f_name: 
        print("application/octect-stream")
    else:
        find_mime(f_name)




def find_mime(name):
   #i have a . in the name
    
    #split the name from the extension
    image = "gif jpg jpeg png"
    appli = "pdf zip"
    plain = "txt"
    pre = name.split('.',1)[0]
    post = name.split('.',1)[1]

    #if the extension belongs to the 'image'string:
    if post in image:
        print("image/"+post)
    elif post in appli:
        print("application/"+post)
    elif post in plain:
        print("plain/text")
    else:
        print("application/octect-stream")
    

main()