#_______OK_______

from fpdf import FPDF

def main():
    name = input("Name: ")
    #make a pdf obj: portrait, a4 format, not auto page breal
    pdf = FPDF(orientation="P", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    #settings for the image title
    pdf.set_font("Helvetica", "B", 24)

    #center the image on the tshirt layout
    pdf.cell(w=0, h=20, txt="CS50 Shirtificate", border=0, ln=1, align="C")

    #add the image and position it
    shirtWidth = 150
    px = (pdf.w - shirtWidth)/ 2
    py = 60
    pdf.image("shirtificate.png", x = px, y =py, w= shirtWidth)

    #add user name as overlay
    pdf.set_font("Helvetica","I", 15)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, py +50)
    pdf.cell(w=0, h=10, txt=name, border=0, ln=1, align="C")

    #save the output in a file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
