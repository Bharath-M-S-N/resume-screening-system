from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):

    """
    Extract text from a PDF file.
    
    parameters:
         file_path(str): path to pdf file
    returns:
         str: Extract text
    """
    text = ""

    reader = PdfReader(file_path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text.strip()