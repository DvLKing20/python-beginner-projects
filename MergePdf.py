import pypdf
import os
from time import strftime,sleep



def PDF_MERGER(USER_PATH,USER_PDF1,USER_PDF2,i):
   try:
        Date = strftime("%Y_%m_%d")
        os.chdir(USER_PATH)
        READER_PDF = pypdf.PdfReader(USER_PDF1)
        READER_PDF2 = pypdf.PdfReader(USER_PDF2)
        WRITER_PDF = pypdf.PdfWriter()
        for page in READER_PDF.pages:
           WRITER_PDF.add_page(page)
        for page in READER_PDF2.pages:
              WRITER_PDF.add_page(page)
        CUSTOM_NAME = input("Want A Custom Name?(press enter for default) : ") or 'merged'+i  
        with open(f'{CUSTOM_NAME}_{Date}.pdf', 'wb') as Output:
         WRITER_PDF.write(Output)
        print(f"DONE(saved as {CUSTOM_NAME}_{Date}.pdf)")
   except Exception:
      print("\nYou Written The Path or Wrong Pdf Name Try again :(\n")


i = None 
while True:
  USER_PATH = input("Enter Your folder Path : ")
  USER_PDF1 = input("Enter First Pdf Name You Want to Merge : ")
  USER_PDF2 = input("Enter Seconnd Pdf Name You Want to Merge : ")     
  print("\nProcessing...")
  sleep(.5)
  PDF_MERGER(USER_PATH,USER_PDF1,USER_PDF2,i)
  i = 0
  i += 1