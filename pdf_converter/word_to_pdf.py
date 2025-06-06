from docx2pdf import convert

def word_to_pdf(word_file, pdf_file):
    # Convert Word document to PDF
    convert(word_file, pdf_file)
    print(f'Successfully converted {word_file} to {pdf_file}')
