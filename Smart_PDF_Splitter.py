from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from datetime import date

today = date.today()




inputpdf = PdfFileReader(open("yapay_zeka.pdf", "rb")) # it should be in same dicroctary

a = int(input('Please input the series number of documentation')) # name of documentation
b = 0
n = int(input("Please input the number that divider")) # n for each pdf

page_number = inputpdf.numPages

rest = page_number%n

for i in range(0, inputpdf.numPages,n):

    if i == inputpdf.numPages-rest:
        for c in range(rest):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i+c))
        filename = "#00-%s_" % str(a+b) + str(today)+".pdf"
        with open(filename, "wb") as outputStream:
            output.write(outputStream)

    else:
        output = PdfFileWriter()

        for d in range(n):
            output.addPage(inputpdf.getPage(i + d))


        filename = "#00-%s_" % str(a+b) + str(today)+".pdf"
        with open(filename, "wb") as outputStream:
            output.write(outputStream)
    b = b+1




