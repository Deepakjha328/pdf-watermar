# add water mark on my all pdf page
import PyPDF2

template =PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark =PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output =PyPDF2.PdfFileWriter()


#looping to all page in pdf file
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('wtrmrkd_output.pdf','wb') as file:
        output.write(file)






