from fpdf import FPDF
import webbrowser
import os
from filestack import Client

API_KEY = 'AYjbzUhVfTyeeqUzq2TaCz'
class PDFReport:
    """Creates pdf file about the data of bill shares by each employee."""

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        pdf = FPDF(orientation='P',unit='pt',format='A4')
        flatmate1_pays = str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate2_pays = str(round(flatmate2.pays(bill,flatmate1),2))
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png",w=30,h=30)

        pdf.set_font(family='Times',size=24,style='B')
        pdf.cell(w=0,h=40,txt="Sachdeva Apartments",border=0,align='C',ln=1)

        pdf.set_font(family='Times',size=16,style='B')
        pdf.cell(w=0,h=40,txt="{} : {}".format("Address","Amrit Vihar, Burari Delhi-110084"),border=0,align='C',ln=1)

        # Period Column
        pdf.cell(w=80,h=50,txt='Period : ',border=0,align='L')
        pdf.cell(w=120,h=50,txt=bill.period,border=0,align='L',ln=1)

        pdf.set_font(family='Times',size=14)
        #Flatmate Columns
        pdf.cell(w=80,h=50,txt=flatmate1.name,border=0,align='L')
        pdf.cell(w=120,h=50,txt=flatmate1_pays,border=0,align='L',ln=1)

        pdf.cell(w=80,h=50,txt=flatmate2.name,border=0,align='L')
        pdf.cell(w=120,h=50,txt=flatmate2_pays,border=0,align='L')
        

        os.chdir("files")
        pdf.output(f"{bill.period}.pdf")

        # To open the pdf file on default browser
        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self,filepath,api_key=API_KEY):
        self.filepath=filepath
        self.api_key=api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath = self.filepath)
        return new_filelink.url

        

