from fpdf import FPDF  # don't forget to install these packages on your computer
from PIL import Image

name = input("Name: ")
pdf = FPDF()  # create instance of the class
pdf.add_page()
pdf.set_font("Times", "B", 54)
pdf.cell(0, 60, 'CS50 Shirtificate', align='C')  # adjust a title
shirt = Image.open('shirtificate.png')  # don't forget to download the picture to the same directory
pdf.image('shirtificate.png', x=0, y=70)  # adjust the picture
pdf.set_text_color(255, 255, 255)
pdf.set_font('Times', '', 36)
shrift = f'{name} took CS50p'
pdf.text(x=45, y=140, txt=shrift)  # it may vary depending on your name's length
pdf.output('shirtificate.pdf')