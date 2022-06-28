import webbrowser
from flat import Bill, Flatmate    
from reports import PDFReport

amount = float(input("Enter total bill amount - "))
period = input("Enter Period for which bill is to be generated - ")

name1 = input("Enter first flatmate name - ")
days_in_house1 = int(input("How many days {} stayed in apartment - ".format(name1)))

name2 = input("Enter second flatmate name - ")
days_in_house2 = int(input("How many days {} stayed in apartment - ".format(name2)))


bill = Bill(amount=amount,period=period)

flatmate1 = Flatmate(name1,days_in_house1)
flatmate2 = Flatmate(name2,days_in_house2)

print(f"{flatmate1.name} pays: ",flatmate1.pays(bill,flatmate2))
print(f"{flatmate2.name} pays: ",flatmate2.pays(bill,flatmate1))

pdf = PDFReport("{}.pdf".format(bill.period))
pdf.generate(flatmate1=flatmate1,flatmate2=flatmate2,bill=bill)

