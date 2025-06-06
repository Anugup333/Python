import fitz  # PyMuPDF
from docx import Document

def pdf_to_word(pdf_file, word_file):
    # Open the PDF
    pdf = fitz.open(pdf_file)
    document = Document()

    # Extract text from each page
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text = page.get_text("text")
        document.add_paragraph(text)

    # Save to Word document
    document.save(word_file)
    print(f'Successfully converted {pdf_file} to {word_file}')
