from reportlab.pdfgen import canvas

def create_pdf():
    path = "/home/kali/Downloads/output.pdf"
    pdf = canvas.Canvas(path)

    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(100, 750, "Hello! PDF saved in Downloads folder.")

    pdf.save()
    print("PDF saved at:", path)

create_pdf()
