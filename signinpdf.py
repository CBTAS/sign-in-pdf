import os
import time
import tempfile
import PyPDF2
import datetime
from reportlab.pdfgen import canvas
from pdfrw import PdfReader
from pdfrw import PdfWriter
from pathlib import Path


def _get_tmp_filename(suffix=".pdf"):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        return fh.name


def signinpdf(pdf, sign, args):
    print(args)
    page_num, x1, y1, width, height = [int(a) for a in args]
    page_num -= 1
    print(page_num)
    print(x1, y1, width, height)
    output_filename = "{}_signed{}".format(*os.path.splitext(pdf))
    print(output_filename)
    pdf_fh = open(pdf, 'rb')
    sig_tmp_fh = None

    pdf1 = PyPDF2.PdfFileReader(pdf_fh)
    writer = PyPDF2.PdfFileWriter()
    sig_tmp_filename = None

    for i in range(0, pdf1.getNumPages()):
        page = pdf1.getPage(i)

        if i == page_num:
            # Create PDF for signature - Criado o PDF para insercao da assinatura
            sig_tmp_filename = _get_tmp_filename()
            c = canvas.Canvas(sig_tmp_filename, pagesize=page.cropBox)
            c.drawImage(sign, x1, y1, width, height, mask='auto')
            c.showPage()
            c.save()

            # Merge PDF in to original page - Mesclagem da pagina temporaria com assinatura com a pagina destino.
            sig_tmp_fh = open(sig_tmp_filename, 'rb')
            sig_tmp_pdf = PyPDF2.PdfFileReader(sig_tmp_fh)
            sig_page = sig_tmp_pdf.getPage(0)
            sig_page.mediaBox = page.mediaBox
            page.mergePage(sig_page)

        writer.addPage(page)

    with open(output_filename, 'wb') as fh:
        writer.write(fh)

    for handle in [pdf_fh, sig_tmp_fh]:
        if handle:
            handle.close()
    if sig_tmp_filename:
        os.remove(sig_tmp_filename)


def main():
 #   
 #   signinpdf('nomedoarquivo.pdf', 'img-assinatura.png', ["Numero de paginas= int", "Posicao X= int", "Posicao Y= int", "Altura da Imagem= int", "Largura da Imagem= list[]"])
 #   Exemplo:
 #   signinpdf(arquivo.pdf, img.png, [10, 300, 100, 150, 50])
    


if __name__ == "__main__":
    main()
