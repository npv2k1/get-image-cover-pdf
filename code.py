import fitz
import os
import fire
pdffile = "docs.pdf"
doc = fitz.open(pdffile)
page = doc.load_page(0)  # number of page
pix = page.get_pixmap()
output = "outfile.png"
pix.save(output)
def get_cover(pdf_file):
    doc = fitz.open(pdf_file)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    output = f"{pdf_file}.png"
    pix.save(output)
list_of_files = os.listdir(".")
for f in list_of_files:
    if f.endswith(".pdf"):
        get_cover(f) 


def hello(name="World"):
  return "Hello %s!" % name


if __name__ == '__main__':
  fire.Fire(hello)
