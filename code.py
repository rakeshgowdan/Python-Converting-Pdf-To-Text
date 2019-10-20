import PyPDF2
pdf=open("example2.pdf","rb")
pdfRead=PyPDF2.PdfFileReader(pdf)
pdfPages=pdfRead.numPages
selectedPages=pdfRead.getPage(pdfPages-1)
#pyPdf2 used with text data 
text=selectedPages.extractText()

file=open(r"C:\Users\Raksh\Documents\GitHub\Python-Converting-Pdf-To-Text\text2.txt","a")
file.writelines(text)
file.close()
print("Done Converting !!")
