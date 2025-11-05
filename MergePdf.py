import pypdf
import os
from time import strftime, sleep


def pdf_merger(user_path, user_pdf1, user_pdf2, i):
    try:
        date = strftime("%Y_%m_%d")
        os.chdir(user_path)
        reader_pdf = pypdf.PdfReader(user_pdf1)
        reader_pdf2 = pypdf.PdfReader(user_pdf2)
        writer_pdf = pypdf.PdfWriter()
        for page in reader_pdf.pages:
            writer_pdf.add_page(page)
        for page in reader_pdf2.pages:
            writer_pdf.add_page(page)
        custom_name = input("Want A Custom Name?(press enter for default) : ") or 'merged' + i
        with open(f'{custom_name}_{date}.pdf', 'wb') as Output:
            writer_pdf.write(Output)
        print(f"DONE(saved as {custom_name}_{date}.pdf)")
    except Exception:
        print("\nYou Written The Path or Wrong Pdf Name Try again :(\n")


i = None
while True:
    USER_PATH = input("Enter Your folder Path : ")
    USER_PDF1 = input("Enter First Pdf Name You Want to Merge : ")
    USER_PDF2 = input("Enter Second Pdf Name You Want to Merge : ")
    print("\nProcessing...")
    sleep(.5)
    pdf_merger(USER_PATH, USER_PDF1, USER_PDF2, i)
    i = 0
    i += 1
