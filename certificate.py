from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from mail import send_mail




def generate_cert(name,email):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.setPageSize((4000, 2000))
    can.setFont('Helvetica-Bold', 60)
    can.drawString(560, 720, name)
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("certificate.pdf", "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    outputStream = open(f"certificates/{name}_{email}_certificate.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    send_mail(name,email)