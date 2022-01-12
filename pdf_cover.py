import fitz
import fire
def get_cover(pdf,png=""):
    """get pdf cover image

    Args:
        pdf (str): pdf filename
        png (str, optional): output pdf filename. Defaults to "".
    """
    doc = fitz.open(pdf)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    output = f"{pdf}_cover.png"
    pix.save(output)
if __name__ == '__main__':
  fire.Fire(get_cover)
