"""Insert your name and see created PDF file with your text on shirt"""


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.multi_cell(60, 10, '\n')
        self.multi_cell(60, 10, '\n')
        self.cell(65)
        pdf.cell(60, 10, '\nShirtificate', new_x="LMARGIN", new_y="NEXT", align='C')


name = input("Name: ")

pdf = PDF()
pdf.add_page()
pdf.image("images\shirtificate.png", 0, 70)
pdf.set_font("helvetica", "B", 20)
pdf.multi_cell(60, 10, '\n')
pdf.multi_cell(60, 10, '\n')
pdf.multi_cell(60, 10, '\n')
pdf.set_text_color(0, 255, 0)
pdf.cell(190, 30, name + ' is cool :)', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.output("images\shirtificate.pdf")
